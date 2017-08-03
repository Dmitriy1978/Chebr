import unittest, time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class regHelp(unittest.TestCase):
    accept_next_alert = True

    def __init__(self, app):
        super ().__init__ ()
        self.app = app




    def registration(self, Name_reg):
        driver = self.app.driver
        self.app.open_home_page ()
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
        driver = self.app.driver
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


    def delete_user(self, Name_adm):
        driver = self.app.driver
        self.accept_next_alert = True
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
        driver.maximize_window ()
        driver.find_element_by_xpath("//a[contains(text(), 'dmitriy117@i.ua')]//parent::span//parent::td//parent::tr//span[@class = 'glyphicon glyphicon-remove']" ).click ()
        time.sleep ( 10 )
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure to delete selected row\(s\)[\s\S]$" )
        time.sleep ( 5 )

    def is_element_present(self, how, what):
        try: self.app.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try:
            self.app.driver.switch_to_alert ()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.app.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

