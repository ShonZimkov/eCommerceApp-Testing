import time
import pytest
from pageObjectsAdmin.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils
from utilities import XLUtils

class Test_002_DDT_Login:
    # basic configuration
    baseURL = ReadConfig.getApplicationURL()
    path = './/TestData/LoginData.xlsx'
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_002_DDT_Login", setup, self.baseURL)
        self.lp = LoginPage(self.driver)
        # get Data from Sheet
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows i a Excel:", self.rows)
        lst_status = []
        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            # Act
            # login
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
        # Assert
            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("*** Test Is Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("*** Test Is Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("*** Test is Failed ***")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("*** Test is Passed ***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test failed ****")
            self.driver.close()
            assert False

        self.logger.info("**** End of Login DDT test ****")
        self.logger.info("******* Completed Test_002_DDT_Login *********")