from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import os

class New_prod(unittest.TestCase):
    accept_next_alert = True

    def __init__(self, app):
        super ().__init__ ()
        self.app = app


    def add_new_prod(self, Text_prod):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[contains(text(),'Продать товар')]").click()
        driver.find_element_by_xpath("//a[@data-id='4859']").click()
        driver.find_element_by_xpath ( "//a[@data-id='4903']" ).click ()
        driver.find_element_by_xpath ( "//a[@data-id='4904']" ).click ()

        driver.find_element_by_xpath ( "//input[@id='content_title']").click()
        driver.find_element_by_xpath ( "//input[@id='content_title']").clear()
        driver.find_element_by_xpath ( "//input[@id='content_title']").send_keys( Text_prod.firstname)

        driver.find_element_by_xpath ( "//input[@id='instance_price']").click()
        driver.find_element_by_xpath ( "//input[@id='instance_price']").clear()
        driver.find_element_by_xpath ( "//input[@id='instance_price']").send_keys(Text_prod.price)

        driver.find_element_by_xpath ( "//input[@id='instance_quantity']").click ()
        driver.find_element_by_xpath ( "//input[@id='instance_quantity']").clear ()
        driver.find_element_by_xpath ( "//input[@id='instance_quantity']").send_keys ( Text_prod.quantity )

        driver.find_element_by_xpath ( "//div[contains(text(), 'руб.')]").click ()
        driver.find_element_by_xpath ( "//li[contains(text(), 'грн')]").click ()


        driver.find_element_by_xpath ( "// textarea[@id='content_text']" ).click ()
        driver.find_element_by_xpath ( "// textarea[@id='content_text']" ).clear ()
        driver.find_element_by_xpath ( "// textarea[@id='content_text']" ).send_keys ( Text_prod.description)

        driver.find_element_by_xpath ( "//div[@id='content_isActive-styler']" ).click ()
        driver.find_element_by_xpath ( "//div[contains(text(), 'United States')]" ).click ()
        driver.find_element_by_xpath ( "//li[contains(text(), 'Canada')]" ).click ()

        driver.find_element_by_xpath ( "//div[@id='properties_obschaja-ploschad-styler']" ).click ()
        driver.find_element_by_xpath ( "//div[@id='properties_obschaja-ploschad-styler']//li[@class='selected sel' and contains(text(),'до 50')]" ).click ()


        element = driver.find_element_by_xpath("//div[@class='b-uploadImage' and child::div[contains(text(), 'Основное фото')]]//input[@name='file']")
        element.send_keys(os.getcwd()+ Text_prod.file)
        time.sleep(5)
        driver.find_element_by_xpath ( "//input[@value='Сохранить']" ).click ()
        driver.maximize_window ()


    def modify_prod(self, Modify_prod):
        driver = self.app.driver
        #entering cabinet
        driver.find_element_by_xpath ( "//a[@class='b-mainNavigation__link' and contains(text(),'Кабинет')]").click ()
        driver.find_element_by_xpath ( "//span[contains(text(),'Мои товары')]" ).click ()
        driver.find_element_by_xpath ( "//a[@class='b-profileFilterTabs__link' and contains(text(),'Созданы')]").click ()
        driver.find_element_by_xpath ( "//a[contains(text(),'Изменить')]" ).click ()

        #change kind of property
        driver.find_element_by_xpath ( "//a[@data-id='4905']" ).click ()

        #change name of property
        driver.find_element_by_xpath ( "//input[@id='content_title']" ).click ()
        driver.find_element_by_xpath ( "//input[@id='content_title']" ).clear ()
        driver.find_element_by_xpath ( "//input[@id='content_title']" ).send_keys ( Modify_prod.firstname )

        # change price of property
        driver.find_element_by_xpath ( "//input[@id='instance_price']" ).click ()
        driver.find_element_by_xpath ( "//input[@id='instance_price']" ).clear ()
        driver.find_element_by_xpath ( "//input[@id='instance_price']" ).send_keys ( Modify_prod.price )

        # change quantity of property
        driver.find_element_by_xpath ( "//input[@id='instance_quantity']" ).click ()
        driver.find_element_by_xpath ( "//input[@id='instance_quantity']" ).clear ()
        driver.find_element_by_xpath ( "//input[@id='instance_quantity']" ).send_keys ( Modify_prod.quantity )

        # change quantity of currency
        driver.find_element_by_xpath ( "//div[contains(text(), 'грн')]" ).click ()
        driver.find_element_by_xpath ( "//li[contains(text(), 'руб.')]" ).click ()

        # change description of property

        self.change_field_value ( Modify_prod )

        #move product to sale
        driver.find_element_by_xpath ( "//div[@id='content_isActive-styler']" ).click ()

        # change country of property
        driver.find_element_by_xpath ( "//div[contains(text(), 'Canada')]" ).click ()
        driver.find_element_by_xpath ( "//li[contains(text(), 'American Samoa')]" ).click ()

        # change square of property
        driver.find_element_by_xpath ( "//div[@id='properties_obschaja-ploschad-styler']" ).click ()
        driver.find_element_by_xpath ( "//div[@id='properties_obschaja-ploschad-styler']//li[@style='white-space: nowrap; display: block;' and contains(text(),'от 50 до 100')]" ).click ()

        #delete photo of property
        #driver.find_element_by_xpath ( "//div[@class='b-uploadImage' and child::div[contains(text(), 'Основное фото')]]//div[@style='user-select: none; display: inline-block; position: relative; overflow: hidden;']" ).click ()
        driver.find_element_by_xpath ("//div[@class='b-uploadImage' and child::div[contains(text(), 'Основное фото')]]//input[@type='checkbox']" ).click ()
        #new photo of property
        element = driver.find_element_by_xpath ("//div[@class='b-uploadImage' and child::div[contains(text(), 'Основное фото')]]//input[@name='file']" )
        element.send_keys ( os.getcwd () + Modify_prod.file )
        time.sleep ( 5 )
        driver.find_element_by_xpath ( "//input[@value='Сохранить']" ).click ()
        driver.maximize_window ()

    def change_field_value(self, Modify_prod):
        driver = self.app.driver
        if Modify_prod.description is not None:
            driver.find_element_by_xpath ( "// textarea[@id='content_text']" ).click ()
            driver.find_element_by_xpath ( "// textarea[@id='content_text']" ).clear ()
            driver.find_element_by_xpath ( "// textarea[@id='content_text']" ).send_keys ( Modify_prod.description )