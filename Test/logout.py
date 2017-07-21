# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://chebr.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Войти").click()
        time.sleep(10)
        driver.find_element_by_id("_login").click()
        driver.find_element_by_id("_login").clear()
        driver.find_element_by_id("_login").send_keys("dmitriy117@i.ua")
        driver.find_element_by_id("_password").click()
        driver.find_element_by_id("_password").clear()
        driver.find_element_by_id("_password").send_keys("11111")
        driver.find_element_by_css_selector("div.b-loginForm__control.-type_submit > input[type=\"submit\"]").click()
        time.sleep(5)
        element_to_hover_over = driver.find_element_by_xpath ( "html/body/div/div[1]/div/ul[2]/li[2]/a" )
        hover = ActionChains ( driver ).move_to_element ( element_to_hover_over )
        hover.perform ()
        # driver.find_element_by_xpath("html/body/div/div[1]/div/ul[2]/li[2]/a").send_keys(Keys.NULL)
        time.sleep ( 5 )
        driver.find_element_by_xpath ( "//a[contains(@href, '/ru/account/logout')]" ).click ()
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
