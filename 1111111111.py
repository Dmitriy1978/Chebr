# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 1111111111(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://chebr.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1111111111(self):
        driver = self.driver
        driver.get(self.base_url + "/ru/profile/products?action=edit")
        driver.find_element_by_link_text(u"Товары для детей").click()
        driver.find_element_by_id("content_title").click()
        driver.find_element_by_id("instance_price").click()
        driver.find_element_by_id("instance_quantity").click()
        driver.find_element_by_css_selector("div.jq-selectbox__select-text").click()
        driver.find_element_by_id("content_text").click()
        driver.find_element_by_css_selector("#entity_countryId-styler > div.jq-selectbox__select > div.jq-selectbox__select-text").click()
        driver.find_element_by_css_selector("#entity_countryId-styler > div.jq-selectbox__dropdown > ul > li.sel.selected").click()
        driver.find_element_by_name("file").click()
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
    
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
