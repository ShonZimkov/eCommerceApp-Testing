import pytest
from selenium import webdriver
from pageObjectsAdmin.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("************ TEST_001_Login *************")
        self.logger.info("************ Verifying Home Page Title *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "Your store. Login":
            assert  True
            self.logger.info("************ Home Page Test Is Passed *************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.error("************ Home Page Test Is Failed *************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************ Verifying Login Test *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************ Login Test Is Passed *************")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/test_login.png")
            self.logger.error("************ Login Test Is Failed *************")
            self.driver.close()
            assert False