from selenium.webdriver.common.by import By
import time
from pageObjectsUserP.LoginPageUserP import LoginUserP
from pageObjectsUserP.OrdersPage import OrdersPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_015_getOrders:
    userloginURL = ReadConfig.getUserLoginURL()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_getOrder(self, setup):
        self.logger.info("************ Starting Test_015_getOrders *************")
        self.logger.info("************ Verifying Login Test *************")
        self.driver = setup
        self.driver.get(self.userloginURL)
        self.driver.maximize_window()

        self.lp = LoginUserP(self.driver)
        self.lp.setUserName("shoniki951@gmail.com")
        self.lp.setPassword("Mamiki11")
        self.lp.clickLogin()

        self.op = OrdersPage(self.driver)
        self.op.clickMyAccount()
        self.logger.info("************ Account Settings Page *************")
        time.sleep(1)
        self.op.clickOrders()
        self.logger.info("************ Orders Page *************")
        time.sleep(1)

        self.logger.info("************ Validate Orders Exist *************")

        act_url = self.driver.current_url
        if act_url == "https://demo.nopcommerce.com/order/history":
            assert True
            self.logger.info("************ Get Orders Test Passed *************")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/test_loginUser.png")
            self.logger.error("************ Get Orders Test Failed *************")
            self.driver.close()
            assert False