import pytest
from pageObjectsAdmin.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils


class Test_001_Login:
    # basic configuration
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_002_HomePage", setup, self.baseURL)

        # Assert
        self.logger.info("************ Verifying Home Page Title *************")
        self.title = self.driver.title
        customUtils.assert_equal_title(self, "Your store. Login", "Test_002_HomePage")
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_001_Login", setup, self.baseURL)
        self.lp = LoginPage(self.driver)

        # Act
        # login
        self.driver.implicitly_wait(2)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # Assert
        self.title = self.driver.title
        customUtils.assert_equal_title(self, "Dashboard / nopCommerce administration", "Test_001_Login")
        self.driver.close()
