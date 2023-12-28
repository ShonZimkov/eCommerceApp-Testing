import time
from selenium.webdriver.common.by import By
from pageObjectsUser.LoginPageUser import LoginUser
from pageObjectsUser.AddToCartPage import AddToCart
from pageObjectsUser.CheckoutPage import CheckoutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_013_Checkout:
    userloginURL = ReadConfig.getUserLoginURL()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_checkout(self, setup):
        self.logger.info("************ Starting Test_013_Checkout  *************")
        self.logger.info("************ Verifying Login  *************")
        self.driver = setup
        self.driver.get(self.userloginURL)
        self.driver.maximize_window()

        self.lp = LoginUser(self.driver)
        self.lp.setUserName("shoniki951@gmail.com")
        self.lp.setPassword("Mamiki11")
        self.lp.clickLogin()

        time.sleep(2)
        self.atc = AddToCart(self.driver)
        self.atc.clickJewelryLink()
        self.logger.info("******** Jewelry Page  *********")
        time.sleep(2)
        self.atc.clickAddToCart()
        self.atc.clickShoppingCart()
        self.logger.info("******** Shopping Cart Page *********")

        self.cbc = CheckoutPage(self.driver)
        self.cbc.clickOnTermsofService()
        self.cbc.clickOnCheckout()
        time.sleep(2)
        self.logger.info("******** Validate Checkout Page *********")

        act_title = self.driver.title
        if act_title == "nopCommerce demo store. Checkout":
            assert True
            self.logger.info("************ Checkout Test Is Passed *************")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/test_checkout.png")
            self.logger.error("************ Checkout Test Is Failed *************")
            self.driver.close()
            assert False