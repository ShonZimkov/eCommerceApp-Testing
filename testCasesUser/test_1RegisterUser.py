import pytest
from selenium.webdriver.common.by import By
from pageObjectsUser.RegisterPageUser import RegisterUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.customUtils import customUtils

class Test_010_RegisterUser:
    # configurations
    userloginURL = ReadConfig.getUserLoginURL()
    logger = LogGen.loggen()

    register_lst = ReadConfig.getRegisterUser()

    @pytest.mark.sanity
    def test_registerUser(self, setup):
        # Arrange
        customUtils.test_start(self, "Test_010_RegisterUser", setup, self.userloginURL)
        self.ru = RegisterUser(self.driver)

        # Act
        # navigate to register page
        self.driver.implicitly_wait(5)
        self.ru.clickOnRegister()
        self.logger.info("******** Register Page ********")

        self.logger.info("******** Starting Register User Test *********")
        self.logger.info("******** Providing User info *******")

        # provide registration info
        self.driver.implicitly_wait(2)
        self.ru.setGender(self.register_lst[0])
        self.ru.setFirstName(self.register_lst[1])
        self.ru.setLastName(self.register_lst[2])
        self.ru.setDob(self.register_lst[3],self.register_lst[4],self.register_lst[5])
        self.ru.setEmail(self.register_lst[6])
        self.ru.setCompanyName(self.register_lst[7])
        self.ru.setPassword(self.register_lst[8])
        self.ru.clickOnRegisterIN()

        self.logger.info("******** Saving User info *********")

        # Assert
        self.logger.info("******** Register user validation *********")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        customUtils.assert_equal_msg(self, 'Your registration completed', "Test_010_RegisterUser")

        self.driver.close()
        self.logger.info("********* Ending Test_010_RegisterUser ********")
