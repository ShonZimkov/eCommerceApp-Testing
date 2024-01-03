import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjectsUser.LoginPageUser import LoginUser
from pageObjectsUser.AddToCartPage import AddToCart
from pageObjectsUser.CheckoutPage import CheckoutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import  customUtils

class Test_014_OrderByCheck:
    # configurations
    userloginURL = ReadConfig.getUserLoginURL()
    username = ReadConfig.getUserUsername()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()
    billing_lst = ReadConfig.getBliingInfo()

    @pytest.mark.regression
    def test_orderByCheck(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_014_OrderByCheck", setup, self.userloginURL)
        self.lp = LoginUser(self.driver)
        self.atc = AddToCart(self.driver)
        self.ckp = CheckoutPage(self.driver)

        # Act
        # login
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # navigate to jewelry page
        self.driver.implicitly_wait(2)
        self.atc.clickJewelryLink()
        self.logger.info("******** Jewelry Page  *********")
        # add item to shopping cart , navigate to shopping cart page
        self.driver.implicitly_wait(2)
        self.atc.clickAddToCart()
        self.driver.implicitly_wait(2)
        self.atc.clickShoppingCart()
        self.logger.info("******** Shopping Cart Page *********")
        # terms of service and navigate to checkout page
        self.ckp.clickOnTermsofService()
        self.ckp.clickOnCheckout()
        self.driver.implicitly_wait(2)
        self.logger.info("******** Billing and Payment Page *********")
        self.logger.info("******** Provide Billing Info *********")

        fname_box_locator = (By.ID, "BillingNewAddress_FirstName")
        # try to input billing information , if there billing information saved then skip
        try:
            fname_box = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(fname_box_locator)
            )
            self.ckp.setFirstName(self.billing_lst[0])
            self.ckp.setLastName(self.billing_lst[1])
            self.ckp.setEmail(self.billing_lst[2])
            self.ckp.setCountry(self.billing_lst[3])
            self.ckp.setCity(self.billing_lst[4])
            self.ckp.setAddress(self.billing_lst[5])
            self.ckp.setPostalCode(self.billing_lst[6])
            self.ckp.setPhoneNumber(self.billing_lst[7])

        except TimeoutException:
            pass
        # navigate to shipping method page
        self.driver.implicitly_wait(2)
        self.ckp.clickBillingContinue()
        self.logger.info("******** Save Billing info *********")
        self.logger.info("******** Shipping Method Page *********")
        # navigate to payment method page
        self.ckp.clickShippingMethodContinue()
        self.logger.info("******** Payment Method Page *********")
        # navigate to payment info page
        self.driver.implicitly_wait(2)
        self.ckp.clickPaymentMethodContinue()
        self.logger.info("******** Payment Info Page *********")
        # navigate to order confirmation page
        self.driver.implicitly_wait(2)
        self.ckp.clickPaymentInfoContinue()
        self.logger.info("******** Order Confirm Page *********")
        # confirm order
        self.driver.implicitly_wait(2)
        self.ckp.clickOrderConfirm()

        # Assert
        self.logger.info("******** Validate Order Confirmation *********")
        self.driver.implicitly_wait(2)
        self.msg = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div/div[1]/strong").text
        customUtils.assert_equal_msg(self, 'Your order has been successfully processed!', "Test_014_OrderByCheck")

        self.driver.close()
        self.logger.info("********* Ending Test_014_OrderByCheck ********")
