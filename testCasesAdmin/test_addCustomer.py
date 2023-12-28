import pytest
import time
from selenium.webdriver.common.by import By
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********* Test_003_AddCustomer *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull ********")

        self.logger.info("******** Starting Add Customer Test *********")

        self.addcust = AddCustomer(self.driver)
        self.driver.implicitly_wait(2)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddNew()
        self.driver.implicitly_wait(2)
        self.logger.info("******** Providing customer info *******")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setFirstName("Shon")
        self.addcust.setLastName("Zimkov")
        self.addcust.setDob("8/9/2000")
        self.addcust.setCompanyName("MoonBridge")
        self.addcust.setAdminContent("This is for testing")
        self.addcust.clickOnSave()

        self.logger.info("******** Saving customer info *********")

        self.logger.info("******** Add customer validation *********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("******* Add customer Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("******* Add customer test failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("********* Ending Test003_AddCustomer ********")


def random_generator(size= 8, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))