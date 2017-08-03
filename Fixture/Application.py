from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

from selenium.webdriver.common.keys import Keys

from Fixture.session import sessionHelperreg
from Fixture.session_ import sessionHelp
from Fixture.registrationHelp import regHelp
from Fixture.Prodhelper import New_prod




class Application(unittest.TestCase):


    def __init__(self):
        super ().__init__ ()
        self.driver = webdriver.Firefox ()
        #self.driver = webdriver.Chrome ()
        self.driver.implicitly_wait ( 30 )
        self.base_url = "http://chebr:testchebr@chebr.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.mail_url = "http://i.ua/"
        self.session = sessionHelperreg( self )
        self.session_ = sessionHelp ( self )
        self.registrationHelp = regHelp(self)
        self.Prodhelper = New_prod(self)





    def open_home_page(self):
        driver = self.driver
        driver.get ( self.base_url + "/ru" )
        #alert = driver.switch_to_alert ()
        #driver.find_element_by_name("Имя пользователя:").sendKeys("chebr")
        #driver.find_element_by_name("Пароль:").sendKeys("chebr")
        #alert.SetAuthenticationCredentials ( "chebr", "testchebr" );
        #alert.send_keys("chebr")
        #alert.send_keys(Keys.TAB)
        #alert.send_keys ( "testchebr" )
        #alert.accept()





    def destroy(self):
        self.driver.quit()

