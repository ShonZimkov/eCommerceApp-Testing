import time
from selenium.webdriver.common.by import By
from pageObjectsUser.RegisterPageUser import RegisterUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Negative Test 11: Register user without last name Error validation
class Test_Negative011_RegisterUserLastNameError:
    userloginURL = ReadConfig.getUserLoginURL()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_registerUserLastNameError(self, setup):
        self.logger.info("********* Test_Negative011_RegisterUserLastNameError *********")
        self.driver = setup
        self.driver.get(self.userloginURL)
        self.driver.maximize_window()

        self.ru = RegisterUser(self.driver)
        time.sleep(1)
        self.ru.clickOnRegister()
        time.sleep(1)
        self.logger.info("******** Register Page ********")

        self.logger.info("******** Starting Register User Last Name Error Test *********")
        self.logger.info("******** Providing User info without Last Name *******")

        self.ru.setGender('Male')
        self.ru.setFirstName('Shon')
        self.ru.setDob('8','September','2000')
        self.ru.setEmail('shoniki951@gmail.com')
        self.ru.setCompanyName('Shon inc')
        self.ru.setPassword('Mamiki11')
        self.ru.clickOnRegisterIN()

        self.logger.info("******** Saving User info without Last name *********")

        self.logger.info("******** Register user Last name error validation *********")

        self.err = self.driver.find_element(By.ID, "LastName-error")

        if self.err:
            assert True == True
            self.logger.info("******* Register user Last name Error Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_registerUserLastNameError_scr.png")
            self.logger.error("******* Register user Last name Error test failed ********")
            assert True == False


        self.driver.close()
        self.logger.info("********* Ending Test_Negative011_RegisterUserLastNameError ********")
