import time
import pytest
from selenium.webdriver.common.by import By
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from pageObjectsAdmin.ExportCustomersPage import ExportCustomers
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Login obj and logger
class Test_Negative004_ExportCustomersSelectError:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

# TEST 4 : Export and Download (Selected) Customer Info IN XML / EXCEL Error validation after not selecting customers
#     @pytest.mark.sanity
    def test_exportCustomersSelectError(self, setup):
        self.logger.info("******** Test_004_ExportCustomersSelectError *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("******* Login Successful *******")

        self.logger.info("******* Starting Export Customer Error Test *******")

        self.addcust = AddCustomer(self.driver)
        time.sleep(2)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("****** Exporting File (Selected) ******")
        self.expcust = ExportCustomers(self.driver)
        time.sleep(1)
        self.expcust.ClickdrpExportBtn()
        self.expcust.ClicklstSelectedXML()
        time.sleep(2)

        self.msg = self.driver.find_element(By.ID, "exportXmlSelected-info").text

        print(self.msg)
        if "No customers selected" in self.msg:
            assert True == True
            self.logger.info("******* Export Selected Customers Error Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_exportCustomersSelectError_scr.png")
            self.logger.error("******* Export Selected Customers Error test failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("********* Ending Test_004_ExportCustomersSelectError ********")
