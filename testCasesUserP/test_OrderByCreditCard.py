import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjectsUserP.LoginPageUserP import LoginUserP
from pageObjectsUserP.AddToCartPage import AddToCart
from pageObjectsUserP.CheckoutPage import CheckoutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_014_OrderByCreditCard:
    userloginURL = ReadConfig.getUserLoginURL()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_orderByCreditCard(self, setup):
        self.logger.info("************ Starting Test_014_OrderByCreditCard *************")
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
        self.atc.clickShoppingCart()
        self.logger.info("******** Shopping Cart Page *********")

        self.cbc = CheckoutPage(self.driver)
        self.cbc.clickOnTermsofService()
        self.cbc.clickOnCheckout()
        time.sleep(2)
        self.logger.info("******** Billing and Payment Page *********")
        self.logger.info("******** Provide Billing Info *********")

        fname_box_locator = (By.ID, "BillingNewAddress_FirstName")

        try:
            fname_box = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(fname_box_locator)
            )
            self.cbc.setFirstName("Shon")
            self.cbc.setLastName("Zimkov")
            self.cbc.setEmail("shoniki951@gmail.com")
            self.cbc.setCountry("Israel")
            self.cbc.setCity("Eilat")
            self.cbc.setAddress("Hasida 4")
            self.cbc.setPostalCode("88000")
            self.cbc.setPhoneNumber("0525052088")

        except TimeoutException:
            pass

        self.cbc.clickBillingContinue()
        time.sleep(2)

        self.logger.info("******** Save Billing info *********")
        self.logger.info("******** Shipping Method Page *********")
        self.cbc.clickShippingMethodContinue()
        self.logger.info("******** Payment Method Page *********")
        time.sleep(2)
        self.cbc.clickOnCreditCard()
        self.cbc.clickPaymentMethodContinue()
        time.sleep(2)
        self.logger.info("******** Payment Info Page *********")
        self.logger.info("******** Providing Credit Card Info  *********")
        self.cbc.setCardHolderName("Shon Zimkov")
        self.cbc.setCardNumber("4111111111111111")
        self.cbc.setExpirationDate("09","2030")
        self.cbc.setCardCode("123")
        self.cbc.clickPaymentInfoContinue()
        self.logger.info("******** Order Confirm Page *********")
        time.sleep(10)
        self.cbc.clickOrderConfirm()

        self.logger.info("******** Validate Order Confirmation *********")
        time.sleep(2)

        self.msg = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div/div[1]/strong").text

        print(self.msg)
        if 'Your order has been successfully processed!' in self.msg:
            assert True == True
            self.logger.info("******* Order By Credit Card Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_orderByCredit_scr.png")
            self.logger.error("******* Order By Credit Card test failed ********")
            assert True == False

        self.driver.close()
