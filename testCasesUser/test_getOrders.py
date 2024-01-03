import pytest
import time
from pageObjectsUser.LoginPageUser import LoginUser
from pageObjectsUser.OrdersPage import OrdersPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils


class Test_015_getOrders:
    # configurations
    userloginURL = ReadConfig.getUserLoginURL()
    username = ReadConfig.getUserUsername()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_getOrder(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_010_RegisterUser", setup, self.userloginURL)
        self.lp = LoginUser(self.driver)
        self.op = OrdersPage(self.driver)

        # Act
        # login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # navigate to my account page
        self.op.clickMyAccount()
        self.logger.info("************ Account Settings Page *************")
        # navigate to my orders page
        self.driver.implicitly_wait(2)
        self.op.clickOrders()
        self.logger.info("************ Orders Page *************")

        # Assert
        self.driver.implicitly_wait(2)
        self.logger.info("************ Validate Orders Exist *************")
        self.title = self.driver.current_url
        customUtils.assert_equal_title(self, 'https://demo.nopcommerce.com/order/history', "Test_015_getOrders")

        self.driver.close()
        self.logger.info("********* Ending Test_015_getOrders ********")
