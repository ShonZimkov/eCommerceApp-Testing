import time
from selenium.webdriver.common.by import By
from pageObjectsAdmin.LoginPage import LoginPage
from pageObjectsAdmin.CatalogPage import CatalogPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# Negative Test 3: testing name is empty error validation in add product
class Test_Negative003_AddProductNameError:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @pytest.mark.sanity
    def test_addProductNameError(self, setup):
        self.logger.info("********* Test_Negative003_AddProductNameError *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfull ********")

        self.logger.info("******** Starting Add Product Name Error Test *********")

        self.cata = CatalogPage(self.driver)
        self.driver.implicitly_wait(2)
        self.cata.clickCataloglink()
        self.cata.clickProductslink()

        time.sleep(2)
        self.cata.clickAddProduct()
        self.cata.clickSaveProduct()
        self.logger.info("******** Add product without name *******")

        self.logger.info("******** Add product Name Error validation *********")

        self.msg = self.driver.find_element(By.XPATH, "//*[@id='product-form']/div[2]").text

        print(self.msg)
        if "Please provide a name" in self.msg:
            assert True == True
            self.logger.info("******* Add product Name Error Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addProductNameError_scr.png")
            self.logger.error("******* Add product Name Error test failed ********")
            assert True == False

        self.driver.close()
        self.logger.info("********* Ending Test_Negative003_AddProductNameError ********")
