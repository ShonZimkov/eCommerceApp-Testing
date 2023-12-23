import time
from selenium.webdriver.common.by import By
from pageObjectsUserP.LoginPageUserP import LoginUserP
from pageObjectsUserP.AddToCartPage import AddToCart
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_012_AddToCart:
    userloginURL = ReadConfig.getUserLoginURL()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_addtocart(self, setup):
        self.logger.info("************ Starting Test_012_AddToCart  *************")
        self.logger.info("************ Verifying Login  *************")
        self.driver = setup
        self.driver.get(self.userloginURL)
        self.driver.maximize_window()

        self.lp = LoginUserP(self.driver)
        self.lp.setUserName("shoniki951@gmail.com")
        self.lp.setPassword("Mamiki11")
        self.lp.clickLogin()

        time.sleep(2)
        self.atc = AddToCart(self.driver)
        self.atc.clickJewelryLink()
        self.logger.info("******** Jewelry Page  *********")
        time.sleep(2)
        self.atc.clickAddToCart()
        self.logger.info("******** Add To Cart validation *********")
        time.sleep(2)

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'The product has been added to your' in self.msg:
            assert True == True
            self.logger.info("******* Add To Cart Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("******* Add To Cart test failed ********")
            assert True == False

        # self.driver.close()
        self.logger.info("********* Ending Test_012_AddToCart ********")

