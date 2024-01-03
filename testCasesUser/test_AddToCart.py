import time
import pytest
from selenium.webdriver.common.by import By
from pageObjectsUser.LoginPageUser import LoginUser
from pageObjectsUser.AddToCartPage import AddToCart
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils


class Test_012_AddToCart:
    # configurations
    userloginURL = ReadConfig.getUserLoginURL()
    username = ReadConfig.getUserUsername()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addtocart(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_012_AddToCart", setup, self.userloginURL)
        self.lp = LoginUser(self.driver)
        self.atc = AddToCart(self.driver)

        # Act
        # login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # navigate to jewelry page
        self.driver.implicitly_wait(2)
        self.atc.clickJewelryLink()
        self.logger.info("******** Jewelry Page  *********")
        # add item to cart
        self.driver.implicitly_wait(2)
        self.atc.clickAddToCart()

        # Assert
        self.logger.info("******** Add To Cart validation *********")
        self.driver.implicitly_wait(2)
        self.msg = self.driver.find_element(By.XPATH, "//*[@id='bar-notification']/div/p").text
        customUtils.assert_equal_msg(self, 'The product has been added to your', "Test_012_AddToCart")

        self.driver.close()
        self.logger.info("********* Ending Test_012_AddToCart ********")

