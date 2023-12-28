import time
from selenium.webdriver.common.by import By
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.CatalogPage import CatalogPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Negative Test 7: testing approve selected records while none chosen error validation
class Test_Negative007_RecordsApproveSelectedError:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_approveSelectedError(self, setup):
        self.logger.info("********* Test_Negative007_RecordsApproveSelectedError *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull ********")

        self.logger.info("******** Starting Approve Selected Records Error Test *********")

        self.cata = CatalogPage(self.driver)
        self.driver.implicitly_wait(2)
        self.cata.clickCataloglink()
        self.cata.clickProductReviewslink()

        time.sleep(2)
        self.cata.clickReportsApproved()
        self.logger.info("******** Approve Selected Records *******")
        time.sleep(1)
        self.logger.info("******** Approve Selected Records Error validation *********")

        self.msg = self.driver.find_element(By.ID, "nothingSelectedAlert-info").text

        print(self.msg)
        if "Please select at least one record" in self.msg:
            assert True == True
            self.logger.info("******* Approve Selected Records Error Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_approveSelectedRecordsError_scr.png")
            self.logger.error("******* Approve Selected Records Error test failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("********* Ending Test_Negative007_RecordsApproveSelectedError ********")