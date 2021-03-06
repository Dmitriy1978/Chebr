# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ConfirmLogin(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome ()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.i.ua/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_confirm_login(self):
        driver = self.driver
        driver.get(self.base_url + "/?_rand=1500369555")
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("dmitriy117@i.ua")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("dmitriy115")
        driver.find_element_by_css_selector("p > input[type=\"submit\"]").click()
        driver.find_element_by_xpath("//div[@id='mesgList']/form/div/a/span[2]").click()
        time.sleep(6)
        mail = driver.find_element_by_xpath("//div[@class = 'message_body']/iframe")
        driver.switch_to_frame(mail)
        driver.find_element_by_xpath("//a[contains(@href, 'http://chebr.com/ru/profile/confirm')]").click()
        driver.switch_to_window(driver.window_handles[-1])
        time.sleep(15)
        driver.find_element_by_link_text ( u"Войти" ).click ()
        time.sleep ( 10 )
        driver.find_element_by_id ( "_login" ).click ()
        driver.find_element_by_id ( "_login" ).clear ()
        driver.find_element_by_id ( "_login" ).send_keys ( "dmitriy117@i.ua" )
        driver.find_element_by_id ( "_password" ).click ()
        driver.find_element_by_id ( "_password" ).clear ()
        driver.find_element_by_id ( "_password" ).send_keys ( "11111" )
        driver.find_element_by_css_selector("div.b-loginForm__control.-type_submit > input[type=\"submit\"]" ).click ()
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
