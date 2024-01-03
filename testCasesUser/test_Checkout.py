import pytest
from utilities.customUtils import customUtils
from pageObjectsUser.LoginPageUser import LoginUser
from pageObjectsUser.AddToCartPage import AddToCart
from pageObjectsUser.CheckoutPage import CheckoutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_013_CheckoutPage:
    userloginURL = ReadConfig.getUserLoginURL()
    username = ReadConfig.getUserUsername()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_checkout(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_013_CheckoutPage", setup, self.userloginURL)
        self.lp = LoginUser(self.driver)
        self.atc = AddToCart(self.driver)
        self.cbc = CheckoutPage(self.driver)

        # Act
        # login
        self.lp.setUserName("shoniki951@gmail.com")
        self.lp.setPassword("Mamiki11")
        self.lp.clickLogin()
        # navigate to jewelry page
        self.driver.implicitly_wait(2)
        self.atc.clickJewelryLink()
        self.logger.info("******** Jewelry Page  *********")
        # add item to cart and navigate to shopping cart
        self.driver.implicitly_wait(2)
        self.atc.clickAddToCart()
        self.atc.clickShoppingCart()
        self.logger.info("******** Shopping Cart Page *********")
        # accept term of service and navigate to checkout page
        self.cbc.clickOnTermsofService()
        self.cbc.clickOnCheckout()
        self.driver.implicitly_wait(2)

        # Assert
        self.logger.info("******** Validate Checkout Page *********")
        self.title = self.driver.title
        customUtils.assert_equal_title(self, "nopCommerce demo store. Checkout", "Test_013_CheckoutPage")

        self.driver.close()
        self.logger.info("********* Ending Test_013_CheckoutPage ********")

