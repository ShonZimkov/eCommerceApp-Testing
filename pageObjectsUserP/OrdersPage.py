from selenium.webdriver.common.by import By


class OrdersPage:

    myAccount_link_xpath = "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a"
    orders_link_xpath = "/html/body/div[6]/div[3]/div/div[1]/div/div[2]/ul/li[3]/a"

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.myAccount_link_xpath).click()

    def clickOrders(self):
        self.driver.find_element(By.XPATH, self.orders_link_xpath).click()