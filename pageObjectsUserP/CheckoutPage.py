from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CheckoutPage:
    boxterms_id = "termsofservice"
    checkout_btn_id = "checkout"
    txtFirstName_id = "BillingNewAddress_FirstName"
    txtLastName_id = "BillingNewAddress_LastName"
    txtEmail_id = "BillingNewAddress_Email"
    drpCountry_id = "BillingNewAddress_CountryId"
    txtCity_id = "BillingNewAddress_City"
    txtAddress_id = "BillingNewAddress_Address1"
    txtPostal_code_id = "BillingNewAddress_ZipPostalCode"
    txtPhone_id = "BillingNewAddress_PhoneNumber"
    billingContinue_button_name = "save"
    shippingMethodContinue_button_xpath = "//*[@id='shipping-method-buttons-container']/button"
    paymentMethodContinue_button_name = "save"
    paymentInfoContinue_button_xpath = "//*[@id='payment-info-buttons-container']/button"
    orderContinue_button_xpath = "//*[@id='confirm-order-buttons-container']/button"

    def __init__(self, driver):
        self.driver = driver

    def clickOnTermsofService(self):
        self.driver.find_element(By.ID, self.boxterms_id).click()

    def clickOnCheckout(self):
        self.driver.find_element(By.ID, self.checkout_btn_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setCountry(self, country):
        drp = Select(self.driver.find_element(By.ID, self.drpCountry_id))
        drp.select_by_visible_text(country)

    def setCity(self, city):
        self.driver.find_element(By.ID, self.txtCity_id).clear()
        self.driver.find_element(By.ID, self.txtCity_id).send_keys(city)
    def setAddress(self, address):
        self.driver.find_element(By.ID, self.txtAddress_id).clear()
        self.driver.find_element(By.ID, self.txtAddress_id).send_keys(address)

    def setPostalCode(self, pcode):
        self.driver.find_element(By.ID, self.txtPostal_code_id).clear()
        self.driver.find_element(By.ID, self.txtPostal_code_id).send_keys(pcode)
    def setPhoneNumber(self, pnum):
        self.driver.find_element(By.ID, self.txtPhone_id).clear()
        self.driver.find_element(By.ID, self.txtPhone_id).send_keys(pnum)

    def clickBillingContinue(self):
        self.driver.find_element(By.NAME, self.billingContinue_button_name).click()

    def clickShippingMethodContinue(self):
        self.driver.find_element(By.XPATH, self.shippingMethodContinue_button_xpath).click()

    def clickPaymentMethodContinue(self):
        self.driver.find_element(By.NAME, self.paymentMethodContinue_button_name).click()

    def clickPaymentInfoContinue(self):
        self.driver.find_element(By.XPATH, self.paymentInfoContinue_button_xpath).click()

    def clickOrderContinue(self):
        self.driver.find_element(By.XPATH, self.orderContinue_button_xpath).click()

