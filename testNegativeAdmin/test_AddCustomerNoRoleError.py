from selenium.webdriver.common.by import By
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Negative Test 2: testing role is empty error validation in add customer
class Test_Negative002_AddCustomerNoRoleError:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_addCustomerNoRoleError(self, setup):
        self.logger.info("********* Test_Negative002_AddCustomerNoRoleError *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull ********")

        self.logger.info("******** Starting Add Customer Role Error Test *********")

        self.addcust = AddCustomer(self.driver)
        self.driver.implicitly_wait(2)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddNew()
        self.driver.implicitly_wait(2)
        self.logger.info("******** Providing customer info without role *******")

        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Registered")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setFirstName("Shon")
        self.addcust.setLastName("Zimkov")
        self.addcust.setDob("8/9/2000")
        self.addcust.setCompanyName("MoonBridge")
        self.addcust.setAdminContent("This is for testing")
        self.addcust.clickOnSave()

        self.logger.info("******** Saving customer info *********")

        self.logger.info("******** Add customer Role Error validation *********")

        self.msg = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div").text

        print(self.msg)
        if "Add the customer to 'Guests' or 'Registered' customer role" in self.msg:
            assert True == True
            self.logger.info("******* Add customer Role Error Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomerRoleError_scr.png")
            self.logger.error("******* Add customer Role Error test failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("********* Ending Test_Negative002_AddCustomerNoRoleError ********")