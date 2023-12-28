import time
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
        time.sleep(2)

        self.logger.info("******** Starting Search Error Test *********")

        self.lu = LoginUser(self.driver)
        self.lu.clickSearch()
        time.sleep(2)
        self.logger.info("******** search error validation *********")

        self.alert_obj = self.driver.switch_to.alert
        self.err = self.alert_obj.text
        self.alert_obj.accept()
        print(self.err)
        if "Please enter some search keyword" in self.err:
            assert True == True
            self.logger.info("******* search Error Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_SearchError_scr.png")
            self.logger.error("******* search Error test failed ********")
            assert True == False


        self.driver.close()
        self.logger.info("********* Ending Test_Negative015_SearchError ********")
