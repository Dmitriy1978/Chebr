# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class DeleteUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://chebr.com/administration/ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_delete_user(self):
        driver = self.driver
        self.delete_user ( driver )

    def delete_user(self, driver):
        driver.get ( self.base_url )
        time.sleep ( 10 )
        driver.find_element_by_id ( "_login" ).clear ()
        driver.find_element_by_id ( "_login" ).send_keys ( "root" )
        driver.find_element_by_id ( "_password" ).clear ()
        driver.find_element_by_id ( "_password" ).send_keys ( "1stEnter" )
        driver.find_element_by_id ( "submit" ).click ()
        driver.find_element_by_link_text ( "Users" ).click ()
        time.sleep ( 10 )
        driver.find_element_by_xpath("//a[contains(text(), 'dmitriy117@i.ua')]//parent::span//parent::td//parent::tr//span[@class = 'glyphicon glyphicon-remove']" ).click ()
        time.sleep ( 10 )
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure to delete selected row\(s\)[\s\S]$" )
        time.sleep ( 5 )

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
