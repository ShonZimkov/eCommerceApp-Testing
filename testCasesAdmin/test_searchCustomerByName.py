import time
import pytest
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from pageObjectsAdmin.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName_005(self, setup):
        self.logger.info("******** SearchCustomerByName_005 *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("******* Login Successful *******")

        self.logger.info("******* Starting Search Customer By Name *******")

        self.addcust = AddCustomer(self.driver)
        time.sleep(2)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        time.sleep(2)
        self.logger.info("****** searching customer by nameID ******")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Steve")
        searchcust.setLastName("Gates")
        searchcust.clickSearch()
        time.sleep(1)
        status = searchcust.searchCustomerByName("Steve Gates")
        assert True == status
        self.logger.info("******** TC_SearchCustomerByName_005 Finished")

        self.driver.close()
