import pytest
from selenium.webdriver.common.by import By
from pageObjectsUser.LoginPageUser import LoginUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils

class Test_011_LoginUser:
    # configurations
    userloginURL = ReadConfig.getUserLoginURL()
    username = ReadConfig.getUserUsername()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginUser(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_011_LoginUser", setup, self.userloginURL)
        self.lp = LoginUser(self.driver)

        # Act
        # login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # Assert
        self.title = self.driver.title
        customUtils.assert_equal_title(self, "nopCommerce demo store", "Test_011_LoginUser")

        self.driver.close()
        self.logger.info("********* Ending Test_011_LoginUser ********")

    def test_logout(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_017_LogoutUser", setup, self.userloginURL)
        self.lp = LoginUser(self.driver)

        # Act
        # login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # logout
        self.lp.clickLogout()

        # Assert
        login_link = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a")
        if login_link:
            assert True
            self.logger.info("************ Logout Test Is Passed *************")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/test_logoutUser.png")
            self.logger.error("************ Logout Test Is Failed *************")
            self.driver.close()
            assert False
