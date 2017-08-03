import unittest, time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from Model.Names_for_login import Name_log


class sessionHelp():


    def __init__(self, app):
        self.app = app


    def Login(self, Name_log):
        driver = self.app.driver
        #self.driver = webdriver.Chrome()
        self.app.open_home_page()
        time.sleep ( 5 )
        driver.find_element_by_link_text ( u"Войти" ).click ()
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
        #self.app.open_home_page()
        #self.app.Login(driver, Name_log(emaillogin="dmitriy117@i.ua", password="11111"))
        element_to_hover_over = driver.find_element_by_xpath ( "html/body/div/div[1]/div/ul[2]/li[2]/a" )
        hover = ActionChains(driver ).move_to_element ( element_to_hover_over )
        hover.perform ()
        time.sleep ( 5 )
        driver.find_element_by_xpath ( "//a[contains(@href, '/ru/account/logout')]" ).click ()
        time.sleep ( 5 )
