import time
import pytest
import os
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from pageObjectsAdmin.ExportCustomersPage import ExportCustomers
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils

# Login obj and logger
class Test_ExportCustomersSelect_007:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

# TEST 7 : Export and Download (Selected) Customer Info IN XML / EXCEL
    @pytest.mark.sanity
    def test_exportCustomersSelect_007(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_ExportCustomersSelect_007", setup, self.baseURL)
        self.lp = LoginPage(self.driver)
        self.addcust = AddCustomer(self.driver)
        self.expcust = ExportCustomers(self.driver)

        # Act
        # login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("******* Login Successful *******")

        self.logger.info("******* Starting Export Customer INFO *******")
        # navigate to customers page
        self.driver.implicitly_wait(2)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("****** Exporting File (Selected) ******")
        # select and export customers to XML file
        self.driver.implicitly_wait(2)
        self.expcust.ClickSelectCustomer()
        self.expcust.ClickdrpExportBtn()
        self.expcust.ClicklstSelectedXML()

        # Assert
        self.driver.implicitly_wait(2)
        download_directory = "C:/Users/shon/Downloads"
        file_name = "customers.xml"
        file_path = os.path.join(download_directory, file_name)
        if os.path.exists(file_path):
            self.logger.info("*********** File downloaded Successfully *********")
            assert True
        else:
            self.logger.info("*********** File downloaded Failed *********")
            assert False

        self.logger.info("******** TC_ExportCustomersSelected_007 Finished")

        self.driver.close()
