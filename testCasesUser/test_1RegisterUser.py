import pytest
import time
from selenium.webdriver.common.by import By
from pageObjectsUser.RegisterPageUser import RegisterUser
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

        self.ru = RegisterUser(self.driver)
        self.ru.clickOnRegister()
        time.sleep(2)
        self.logger.info("******** Register Page ********")

        self.logger.info("******** Starting Register User Test *********")
        self.logger.info("******** Providing User info *******")

        self.ru.setGender('Male')
        self.ru.setFirstName('Shon')
        self.ru.setLastName('Zimkov')
        self.ru.setDob('8','September','2000')
        self.ru.setEmail('shoniki951@gmail.com')
        self.ru.setCompanyName('Shon inc')
        self.ru.setPassword('Mamiki11')
        self.ru.clickOnRegisterIN()

        self.logger.info("******** Saving User info *********")

        self.logger.info("******** Register user validation *********")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'Your registration completed' in self.msg:
            assert True == True
            self.logger.info("******* Register user Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_registerUser_scr.png")
            self.logger.error("******* Register user test failed ********")
            assert True == False


        self.driver.close()
        self.logger.info("********* Ending Test_010_RegisterUser ********")
