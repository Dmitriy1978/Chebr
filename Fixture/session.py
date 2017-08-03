import unittest, time
from selenium.webdriver.common.action_chains import ActionChains


class sessionHelperreg():


    def __init__(self, app):
        self.app = app


    def Login(self, Name_log):
        driver = self.app.driver
        time.sleep ( 5 )
        driver.find_element_by_id ( "_login" ).click ()
        driver.find_element_by_id ( "_login" ).clear ()
        driver.find_element_by_id ( "_login" ).send_keys ( Name_log.emaillogin )
        driver.find_element_by_id ( "_password" ).click ()
        driver.find_element_by_id ( "_password" ).clear ()
        driver.find_element_by_id ( "_password" ).send_keys ( Name_log.password )
        driver.find_element_by_css_selector("div.b-loginForm__control.-type_submit > input[type=\"submit\"]" ).click ()
        time.sleep ( 5 )

    def Logout_any(self):
        driver = self.app.driver
        element_to_hover_over = driver.find_element_by_xpath ( "html/body/div/div[1]/div/ul[2]/li[2]/a" )
        hover = ActionChains(driver ).move_to_element ( element_to_hover_over )
        hover.perform ()
        time.sleep ( 5 )
        driver.find_element_by_xpath ( "//a[contains(@href, '/ru/account/logout')]" ).click ()
        time.sleep ( 5 )



