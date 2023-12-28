from selenium.webdriver.common.by import By
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Negative Test 1: testing email is empty error validation in add customer
class Test_Negative001_AddCustomerEmailError:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_addCustomerEmailError(self, setup):
        self.logger.info("********* Test_Negative001_AddCustomerEmailError *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull ********")

        self.logger.info("******** Starting Add Customer Email Error Test *********")

        self.addcust = AddCustomer(self.driver)
        self.driver.implicitly_wait(2)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddNew()
        self.driver.implicitly_wait(2)
        self.logger.info("******** Providing customer info without email *******")

        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setFirstName("Shon")
        self.addcust.setLastName("Zimkov")
        self.addcust.setDob("8/9/2000")
        self.addcust.setCompanyName("MoonBridge")
        self.addcust.setAdminContent("This is for testing")
        self.addcust.clickOnSave()

        self.logger.info("******** Saving customer info *********")

        self.logger.info("******** Add customer Email Error validation *********")

        self.msg = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]").text

        print(self.msg)
        if "Email is not entered" in self.msg:
            assert True == True
            self.logger.info("******* Add customer Email Error Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomerEmailError_scr.png")
            self.logger.error("******* Add customer Email Error test failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("********* Ending Test_Negative001_AddCustomerEmailError ********")