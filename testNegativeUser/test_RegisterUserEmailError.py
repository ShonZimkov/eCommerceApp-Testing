import time
from selenium.webdriver.common.by import By
from pageObjectsUser.RegisterPageUser import RegisterUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Negative Test 12: Register user without email Error validation
class Test_Negative012_RegisterUserEmailError:
    userloginURL = ReadConfig.getUserLoginURL()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_registerUserEmailError(self, setup):
        self.logger.info("********* Test_Negative012_RegisterUserEmailError *********")
        self.driver = setup
        self.driver.get(self.userloginURL)
        self.driver.maximize_window()

        self.ru = RegisterUser(self.driver)
        time.sleep(1)
        self.ru.clickOnRegister()
        time.sleep(1)
        self.logger.info("******** Register Page ********")

        self.logger.info("******** Starting Register User email Error Test *********")
        self.logger.info("******** Providing User info without email *******")

        self.ru.setGender('Male')
        self.ru.setFirstName('Shon')
        self.ru.setLastName('Zimkov')
        self.ru.setDob('8','September','2000')
        self.ru.setCompanyName('Shon inc')
        self.ru.setPassword('Mamiki11')
        self.ru.clickOnRegisterIN()

        self.logger.info("******** Saving User info without email *********")

        self.logger.info("******** Register user email error validation *********")

        self.err = self.driver.find_element(By.ID, "Email-error")

        if self.err:
            assert True == True
            self.logger.info("******* Register user email Error Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_registerUserEmailError_scr.png")
            self.logger.error("******* Register user email Error test failed ********")
            assert True == False


        self.driver.close()
        self.logger.info("********* Ending Test_Negative012_RegisterUserEmailError ********")
