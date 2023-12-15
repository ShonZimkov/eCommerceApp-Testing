import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_008_EditCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_editCustomer_008(self, setup):
        self.logger.info("********* Test_008_EditCustomer *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull ********")

        self.logger.info("******** Starting Edit Customer Test *********")

        self.editcust = AddCustomer(self.driver)
        time.sleep(2)
        self.editcust.clickOnCustomerMenu()
        self.editcust.clickOnCustomerMenuItem()
        time.sleep(2)
        self.editcust.clickEditCustomer()
        time.sleep(2)

        self.logger.info("******** Editing customer info *******")

        self.email = random_generator() + "@gmail.com"
        self.editcust.setEmail(self.email)
        self.editcust.setPassword("test123")
        self.editcust.setCustomerRoles("Guests")
        self.editcust.setManagerOfVendor("Vendor 2")
        self.editcust.setFirstName("Shon")
        self.editcust.setLastName("Zimkov")
        self.editcust.setDob("8/9/2000")
        self.editcust.setCompanyName("MoonBridge")
        self.editcust.setAdminContent("This is for testing")
        self.editcust.clickOnSave()

        self.logger.info("******** Saving customer info *********")

        self.logger.info("******** Edit customer validation *********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been updated successfully' in self.msg:
            assert True == True
            self.logger.info("******* Edit customer Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_editCustomer_scr.png")
            self.logger.error("******* Edit customer test failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("********* Ending Test008_editCustomer ********")


def random_generator(size= 8, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))