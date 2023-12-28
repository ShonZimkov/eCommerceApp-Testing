import time

from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from pageObjectsUser.LoginPageUser import LoginUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Negative Test 15: Search empty box Error validation
class Test_Negative015_SearchError:
    userloginURL = ReadConfig.getUserLoginURL()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_registerUserEmailError(self, setup):
        self.logger.info("********* Test_Negative015_SearchError *********")
        self.driver = setup
        self.driver.get(self.userloginURL)
        self.driver.maximize_window()

        self.logger.info("******** Starting Search Error Test *********")

        self.lu = LoginUser(self.driver)
        # self.lu.clickSearch()

        self.logger.info("******** search error validation *********")

        # self.err = self.driver.find_element(By.ID, "Email-error")

        # self.message_element = self.driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button")
        # self.accept_button_message = self.driver.execute_script("return arguments[0].validationMessage", self.message_element)
        # print("Message : ", self.accept_button_message)
        try:
            self.lu.clickSearch()
        except UnexpectedAlertPresentException as e:
            self.logger.info('[!] Error: ' + str(e))

        # if self.message_element:
        #     assert True == True
        #     self.logger.info("******* search Error Test Passed *******")
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_SearchError_scr.png")
        #     self.logger.error("******* search Error test failed ********")
        #     assert True == False


        # self.driver.close()
        self.logger.info("********* Ending Test_Negative015_SearchError ********")
