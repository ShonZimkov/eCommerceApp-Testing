import time
from selenium.webdriver.common.by import By
from pageObjectsUser.RegisterPageUser import RegisterUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Negative Test 13: Register user without password Error validation
class Test_Negative013_RegisterUserPasswordError:
    userloginURL = ReadConfig.getUserLoginURL()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_registerUserPasswordError(self, setup):
        self.logger.info("********* Test_Negative013_RegisterUserPasswordError *********")
        self.driver = setup
        self.driver.get(self.userloginURL)
        self.driver.maximize_window()

        self.ru = RegisterUser(self.driver)
        time.sleep(1)
        self.ru.clickOnRegister()
        time.sleep(1)
        self.logger.info("******** Register Page ********")

        self.logger.info("******** Starting Register User Password Error Test *********")
        self.logger.info("******** Providing User info without Password *******")

        self.ru.setGender('Male')
        self.ru.setFirstName('Shon')
        self.ru.setLastName('Zimkov')
        self.ru.setDob('8','September','2000')
        self.ru.setEmail('shoniki951@gmail.com')
        self.ru.setCompanyName('Shon inc')
        self.ru.clickOnRegisterIN()

        self.logger.info("******** Saving User info without Password *********")

        self.logger.info("******** Register user Password error validation *********")

        self.err = self.driver.find_element(By.ID, "Password-error")

        if self.err:
            assert True == True
            self.logger.info("******* Register user Password Error Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_registerUserFirstNameError_scr.png")
            self.logger.error("******* Register user Password Error test failed ********")
            assert True == False


        self.driver.close()
        self.logger.info("********* Ending Test_Negative013_RegisterUserPasswordError ********")

    # Negative Test 14: Register user without password confirmation Error validation
    def test_registerUserPasswordConfirmationError(self, setup):
        self.logger.info("********* Test_Negative014_RegisterUserPasswordConfError *********")
        self.driver = setup
        self.driver.get(self.userloginURL)
        self.driver.maximize_window()

        self.ru = RegisterUser(self.driver)
        time.sleep(1)
        self.ru.clickOnRegister()
        time.sleep(1)
        self.logger.info("******** Register Page ********")

        self.logger.info("******** Starting Register User Password confirmation Error Test *********")
        self.logger.info("******** Providing User info without Password confirmation *******")

        self.ru.setGender('Male')
        self.ru.setFirstName('Shon')
        self.ru.setLastName('Zimkov')
        self.ru.setDob('8', 'September', '2000')
        self.ru.setEmail('shoniki951@gmail.com')
        self.ru.setCompanyName('Shon inc')
        self.ru.clickOnRegisterIN()

        self.logger.info("******** Saving User info without Password confirmation *********")

        self.logger.info("******** Register user Password confirmation error validation *********")

        self.err = self.driver.find_element(By.ID, "ConfirmPassword-error")

        if self.err:
            assert True == True
            self.logger.info("******* Register user Password confirmation Error Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_registerUserPasswordConfError_scr.png")
            self.logger.error("******* Register user Password confirmation Error test failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("********* Ending Test_Negative014_RegisterUserPasswordConfError ********")
