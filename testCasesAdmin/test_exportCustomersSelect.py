import time
import pytest
import os
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from pageObjectsAdmin.ExportCustomersPage import ExportCustomers
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Login obj and logger
class Test_ExportCustomersSelect_007:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

# TEST 7 : Export and Download (Selected) Customer Info IN XML / EXCEL
    @pytest.mark.sanity
    def test_exportCustomersSelect_007(self, setup):
        self.logger.info("******** ExportCustomersSelect_007 *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("******* Login Successful *******")

        self.logger.info("******* Starting Export Customer INFO *******")

        self.addcust = AddCustomer(self.driver)
        time.sleep(2)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("****** Exporting File (Selected) ******")
        expcust = ExportCustomers(self.driver)
        time.sleep(1)
        expcust.ClickSelectCustomer()
        expcust.ClickdrpExportBtn()
        expcust.ClicklstSelectedXML()
        time.sleep(2)
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
