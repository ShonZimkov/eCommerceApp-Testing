import time
from selenium.webdriver.common.by import By
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.CatalogPage import CatalogPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Negative Test 6: testing name is empty error validation in add manufacturer
class Test_Negative006_AddManufacturerNameError:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_addManufacturerNameError(self, setup):
        self.logger.info("********* Test_Negative006_AddManufacturerNameError *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull ********")

        self.logger.info("******** Starting Add Manufacturer Name Error Test *********")

        self.cata = CatalogPage(self.driver)
        self.driver.implicitly_wait(2)
        self.cata.clickCataloglink()
        self.cata.clickManufacturerslink()

        time.sleep(2)
        self.cata.clickAddManufacturer()
        self.cata.clickSaveManufacturer()
        self.logger.info("******** Add manufacturer without name *******")

        self.logger.info("******** Add manufacturer Name Error validation *********")

        self.msg = self.driver.find_element(By.XPATH, "//*[@id='manufacturer-form']/div[2]").text

        print(self.msg)
        if "Please provide a name" in self.msg:
            assert True == True
            self.logger.info("******* Add manufacturer Name Error Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addManufacturerNameError_scr.png")
            self.logger.error("******* Add manufacturer Name Error test failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("********* Ending Test_Negative006_AddManufacturerNameError ********")
