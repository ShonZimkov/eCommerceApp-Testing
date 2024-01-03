import pytest
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from pageObjectsAdmin.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils

class Test_SearchCustomerByName_005:
    # basic configuration
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # search customer configuration
    fname = ReadConfig.getSearchFirstName()
    lname = ReadConfig.getSearchLastName()

    @pytest.mark.regression
    def test_searchCustomerByName_005(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_SearchCustomerByName_005", setup, self.baseURL)
        self.lp = LoginPage(self.driver)
        self.addcust = AddCustomer(self.driver)
        self.searchcust = SearchCustomer(self.driver)

        # Act
        # login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("******* Login Successful *******")
        self.logger.info("******* Starting Search Customer By Name *******")
        # navigate to customers page
        self.driver.implicitly_wait(2)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        # search customer by name
        self.driver.implicitly_wait(2)
        self.logger.info("****** searching customer by nameID ******")
        self.searchcust.setFirstName(self.fname)
        self.searchcust.setLastName(self.lname)
        self.searchcust.clickSearch()

        # Assert
        self.driver.implicitly_wait(2)
        status = self.searchcust.searchCustomerByName(self.fname + " " + self.lname)
        assert True == status
        self.logger.info("******** TC_SearchCustomerByName_005 Finished")

        self.driver.close()
