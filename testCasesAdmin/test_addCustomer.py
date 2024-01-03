import pytest
from selenium.webdriver.common.by import By
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils
import string
import random

class Test_003_AddCustomer:
    # basic configuration
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # customer configuration
    addcust_lst = ReadConfig.getAddCustomer()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_003_AddCustomer", setup, self.baseURL)
        self.lp = LoginPage(self.driver)
        self.addcust = AddCustomer(self.driver)

        # Act
        # login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull ********")

        self.logger.info("******** Starting Add Customer Test *********")

        # navigate to customers page
        self.driver.implicitly_wait(10)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        # navigate to add customer page
        self.driver.implicitly_wait(2)
        self.addcust.clickOnAddNew()
        self.logger.info("******** Providing customer info *******")

        # provide info for adding new customer
        self.driver.implicitly_wait(2)
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword(self.addcust_lst[0])
        self.addcust.setCustomerRoles(self.addcust_lst[1])
        self.addcust.setManagerOfVendor(self.addcust_lst[2])
        self.addcust.setFirstName(self.addcust_lst[3])
        self.addcust.setLastName(self.addcust_lst[4])
        self.addcust.setDob(self.addcust_lst[5])
        self.addcust.setCompanyName(self.addcust_lst[6])
        self.addcust.setAdminContent(self.addcust_lst[7])
        self.addcust.clickOnSave()

        self.logger.info("******** Saving customer info *********")

        # Assert
        self.logger.info("******** Add customer validation *********")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        customUtils.assert_equal_msg(self, 'customer has been added successfully', "test_addCustomer")

        self.driver.close()
        self.logger.info("********* Ending Test003_AddCustomer ********")


def random_generator(size= 8, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))