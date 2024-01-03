from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class customUtils:
    @staticmethod
    def test_start(self, test_name, setup, url):
        self.logger.info("*********  " + test_name + "  *********")
        self.driver = setup
        self.driver.get(url)
        self.driver.maximize_window()

    @staticmethod
    def assert_equal_msg(self, expected, test_name):
        if expected in self.msg:
            assert True == True
            self.logger.info("*******  " + test_name + "  Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + test_name + "_scr.png")
            self.logger.error("*******  " + test_name + "  failed ********")
            assert True == False
    @staticmethod
    def assert_equal_title(self, expected, test_name):
        if self.title == expected:
            assert True == True
            self.logger.info("*******  " + test_name + "  Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + test_name + "_scr.png")
            self.logger.error("*******  " + test_name + "  failed ********")
            assert True == False
