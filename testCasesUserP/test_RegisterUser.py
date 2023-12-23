import pytest
import time
from selenium.webdriver.common.by import By
from pageObjectsUserP.RegisterPageUserP import RegisterUserP
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_010_RegisterUser:
    userloginURL = ReadConfig.getUserLoginURL()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_registerUser(self, setup):
        self.logger.info("********* Test_010_RegisterUser *********")
        self.driver = setup
        self.driver.get(self.userloginURL)
        self.driver.maximize_window()

        self.rup = RegisterUserP(self.driver)
        self.rup.clickOnRegister()
        time.sleep(2)
        self.logger.info("******** Register Page ********")

        self.logger.info("******** Starting Register User Test *********")
        self.logger.info("******** Providing User info *******")

        self.rup.setGender('Male')
        self.rup.setFirstName('Shon')
        self.rup.setLastName('Zimkov')
        self.rup.setDob('8','September','2000')
        self.rup.setEmail('shoniki951@gmail.com')
        self.rup.setCompanyName('Shon inc')
        self.rup.setPassword('Mamiki11')
        self.rup.clickOnRegisterIN()

        self.logger.info("******** Saving User info *********")

        self.logger.info("******** Register user validation *********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'Your registration completed' in self.msg:
            assert True == True
            self.logger.info("******* Register user Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("******* Register user test failed ********")
            assert True == False


        # self.driver.close()
        self.logger.info("********* Ending Test_010_RegisterUser ********")
