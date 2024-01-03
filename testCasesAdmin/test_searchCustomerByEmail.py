import pytest
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from pageObjectsAdmin.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils

class Test_SearchCustomerByEmail_004:
    # basic configuration
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # search customer configuration
    search_email = ReadConfig.getSearchEmail()

    @pytest.mark.regression
    def test_searchCustomerByEmail_004(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_SearchCustomerByEmail_004", setup, self.baseURL)
        self.lp = LoginPage(self.driver)
        self.addcust = AddCustomer(self.driver)
        self.searchcust = SearchCustomer(self.driver)

        # Act
        # login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("******* Login Successful *******")

        self.logger.info("******* Starting Search Customer By Email *******")
        # navigate to customers page
        self.driver.implicitly_wait(2)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        # search for customer
        self.driver.implicitly_wait(2)
        self.logger.info("****** searching customer by emailID ******")
        self.searchcust.setEmail(self.search_email)
        self.searchcust.clickSearch()

        # Assert
        self.driver.implicitly_wait(2)
        status = self.searchcust.searchCustomerByEmail(self.search_email)
        assert True == status
        self.logger.info("******** TC_SearchCustomerByEmail_004 Finished")

        self.driver.close()
