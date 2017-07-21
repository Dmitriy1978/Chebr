from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re


class Application(unittest.TestCase):

    def __init__(self):
        super ().__init__ ()
        self.driver = webdriver.Firefox ()
        self.driver.implicitly_wait ( 30 )
        self.base_url = "http://chebr.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.mail_url = "http://i.ua/"


    def registration(self, Name_reg):
        driver = self.driver
        self.open_home_page ()
        driver.find_element_by_link_text ( u"Зарегистрироваться" ).click ()
        time.sleep ( 5 )
        driver.find_element_by_xpath ( "//div[@id='account_type0-styler']/div" ).click ()
        driver.find_element_by_id ( "account_firstName" ).click ()
        driver.find_element_by_id ( "account_firstName" ).clear ()
        driver.find_element_by_id ( "account_firstName" ).send_keys ( Name_reg.firstname )
        driver.find_element_by_id ( "account_lastName" ).click ()
        driver.find_element_by_id ( "account_lastName" ).clear ()
        driver.find_element_by_id ( "account_lastName" ).send_keys ( Name_reg.lastname )
        driver.find_element_by_id ( "user_username" ).click ()
        driver.find_element_by_id ( "user_username" ).clear ()
        driver.find_element_by_id ( "user_username" ).send_keys ( Name_reg.username )
        driver.find_element_by_id ( "user_email" ).click ()
        driver.find_element_by_id ( "user_email" ).clear ()
        driver.find_element_by_id ( "user_email" ).send_keys ( Name_reg.emaillogin )
        driver.find_element_by_id ( "address_phone1" ).click ()
        driver.find_element_by_id ( "address_phone1" ).clear ()
        driver.find_element_by_id ( "address_phone1" ).send_keys ( Name_reg.phone )
        driver.find_element_by_id ( "user_password" ).click ()
        driver.find_element_by_id ( "user_password" ).clear ()
        driver.find_element_by_id ( "user_password" ).send_keys ( Name_reg.password )
        time.sleep ( 5 )
        driver.find_element_by_id ( "account_gender0-styler" ).click ()
        time.sleep ( 5 )
        driver.find_element_by_css_selector ( "div.jq-checkbox__div" ).click ()
        time.sleep ( 5 )
        driver.find_element_by_id ( "_notificate-styler" ).click ()
        time.sleep ( 5 )
        driver.find_element_by_css_selector("div.b-registrationForm__control.-type_submit > input[type=\"submit\"]" ).click ()
        time.sleep ( 5 )

    def confirm_login(self, Name_conf):
        driver = self.driver
        driver.get ( "http://www.i.ua/" + "/?_rand=1500369555" )
        driver.find_element_by_name ( "login" ).clear ()
        driver.find_element_by_name ( "login" ).send_keys ( Name_conf.emaillogin )
        driver.find_element_by_name ( "pass" ).clear ()
        driver.find_element_by_name ( "pass" ).send_keys ( Name_conf.passwordf )
        driver.find_element_by_css_selector ( "p > input[type=\"submit\"]" ).click ()
        # driver.find_element_by_xpath ( "//div[@id='mesgList']/form/div/a/span[2]" ).click ()
        driver.find_element_by_xpath ( "//html/body/div[1]/div[5]/div[2]/div[2]/div[2]/form/div[1]/a/span[2]" ).click ()
        time.sleep ( 6 )
        mail = driver.find_element_by_xpath ( "//div[@class = 'message_body']/iframe" )
        driver.switch_to_frame ( mail )
        driver.find_element_by_xpath ( "//a[contains(@href, 'http://chebr.com/ru/profile/confirm')]" ).click ()
        driver.switch_to_window ( driver.window_handles[-1] )
        time.sleep ( 15 )

    def Login(self, Name_log):
        driver = self.driver
        # self.driver = webdriver.Chrome()
        # self.open_home_page ( driver )
        # driver.find_element_by_link_text ( u"Войти" ).click ()
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
        driver = self.driver
        # self.open_home_page ( driver )
        # self.Login(driver, Name_log(emaillogin="dmitriy117@i.ua", password="11111"))
        element_to_hover_over = driver.find_element_by_xpath ( "html/body/div/div[1]/div/ul[2]/li[2]/a" )
        hover = ActionChains ( driver ).move_to_element ( element_to_hover_over )
        hover.perform ()
        time.sleep ( 5 )
        driver.find_element_by_xpath ( "//a[contains(@href, '/ru/account/logout')]" ).click ()
        time.sleep ( 5 )

    def open_home_page(self):
        driver = self.driver
        driver.get ( self.base_url + "/ru" )


    def delete_user(self, Name_adm):
        driver = self.driver
        self.base_url = "http://chebr.com/administration/ru/"
        driver.get(self.base_url)
        time.sleep ( 10 )
        driver.find_element_by_id ( "_login" ).clear ()
        driver.find_element_by_id ( "_login" ).send_keys (Name_adm.logina )
        driver.find_element_by_id ( "_password" ).clear ()
        driver.find_element_by_id ( "_password" ).send_keys (Name_adm.passworda)
        driver.find_element_by_id ( "submit" ).click ()
        driver.find_element_by_link_text ( "Users" ).click ()
        time.sleep ( 10 )
        driver.find_element_by_xpath("//a[contains(text(), 'dmitriy117@i.ua')]//parent::span//parent::td//parent::tr//span[@class = 'glyphicon glyphicon-remove']" ).click ()
        time.sleep ( 10 )
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure to delete selected row\(s\)[\s\S]$" )
        time.sleep ( 5 )

    def destroy(self):
        self.driver.quit()

