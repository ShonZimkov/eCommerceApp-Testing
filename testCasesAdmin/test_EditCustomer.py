import pytest
import time
from selenium.webdriver.common.by import By
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils
import string
import random

class Test_008_EditCustomer:
    # basic configuration
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # edit customer configuration
    editcust_lst = ReadConfig.getAddCustomer()
    @pytest.mark.sanity
    def test_editCustomer_008(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_008_EditCustomer", setup, self.baseURL)
        self.lp = LoginPage(self.driver)
        self.editcust = AddCustomer(self.driver)

        # Act
        # login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull ********")

        self.logger.info("******** Starting Edit Customer Test *********")

        # navigate to customers page
        self.driver.implicitly_wait(2)
        self.editcust.clickOnCustomerMenu()
        self.editcust.clickOnCustomerMenuItem()

        # navigate to edit customer page
        self.driver.implicitly_wait(3)
        self.editcust.clickEditCustomer()

        self.logger.info("******** Editing customer info *******")

        # provide info for edit customer
        self.email = random_generator() + "@gmail.com"
        self.editcust.setEmail(self.email)
        self.editcust.setPassword(self.editcust_lst[0])
        self.editcust.setCustomerRoles(self.editcust_lst[1])
        self.editcust.setManagerOfVendor(self.editcust_lst[2])
        self.editcust.setFirstName(self.editcust_lst[3])
        self.editcust.setLastName(self.editcust_lst[4])
        self.editcust.setDob(self.editcust_lst[5])
        self.editcust.setCompanyName(self.editcust_lst[6])
        self.editcust.setAdminContent(self.editcust_lst[7])
        self.editcust.clickOnSave()

        self.logger.info("******** Saving customer info *********")
        # Assert
        self.logger.info("******** Edit customer validation *********")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        customUtils.assert_equal_msg(self, 'customer has been updated successfully', "test_editCustomer")

        self.driver.close()
        self.logger.info("********* Ending Test008_editCustomer ********")

def random_generator(size= 8, chars= string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))