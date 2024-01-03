import time
import pytest
import os
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from pageObjectsAdmin.ExportCustomersPage import ExportCustomers
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils

class Test_ExportCustomersAll_006:
    # basic configuration
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

#TEST 6 : Export and Download Customer Info IN XML / EXCEL
    @pytest.mark.sanity
    def test_exportCustomersAll_006(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_ExportCustomersAll_006", setup, self.baseURL)
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
        # navigate to customers info
        self.driver.implicitly_wait(2)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        # export customer to XML file
        self.driver.implicitly_wait(2)
        self.logger.info("****** Exporting File (ALL) ******")
        self.expcust.ClickdrpExportBtn()
        self.expcust.ClicklstAllFoundXML()
        self.driver.implicitly_wait(2)

        # Assert
        download_directory = "C:/Users/shon/Downloads"
        file_name = "customers.xml"
        file_path = os.path.join(download_directory, file_name)
        if os.path.exists(file_path):
            self.logger.info("*********** File downloaded Successfully *********")
            assert True
        else:
            self.logger.info("*********** File downloaded Failed *********")
            assert False

        self.driver.close()
        self.logger.info("******** TC_ExportCustomersAll_006 Finished")
