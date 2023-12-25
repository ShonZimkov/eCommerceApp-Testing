from selenium.webdriver.common.by import By
from pageObjectsUserP.LoginPageUserP import LoginUserP
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_011_LoginUserP:
    userloginURL = ReadConfig.getUserLoginURL()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_loginUser(self, setup):
        self.logger.info("************ Verifying Login Test *************")
        self.driver = setup
        self.driver.get(self.userloginURL)
        self.lp = LoginUserP(self.driver)
        self.lp.setUserName("shoniki951@gmail.com")
        self.lp.setPassword("Mamiki11")
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "nopCommerce demo store":
            assert True
            self.logger.info("************ Login Test Is Passed *************")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/test_loginUser.png")
            self.logger.error("************ Login Test Is Failed *************")
            self.driver.close()
            assert False

    def test_logout(self, setup):
        self.logger.info("************ Verifying Logout Test *************")
        self.driver = setup
        self.driver.get(self.userloginURL)
        self.lp = LoginUserP(self.driver)
        self.lp.setUserName("shoniki951@gmail.com")
        self.lp.setPassword("Mamiki11")
        self.lp.clickLogin()
        self.lp.clickLogout()

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
