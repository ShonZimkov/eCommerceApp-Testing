from selenium.webdriver.common.by import By
class AddToCart:
# add to cart page elements and functions
    jewelry_link_xpath = "/html/body/div[6]/div[2]/ul[1]/li[6]"
    addToCart_btn_xpath = "/html/body/div[6]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[3]/div[2]/button[1]"
    shoppingcart_btn_xpath = "//*[@id='topcartlink']/a/span[1]"


    def __init__(self,driver):
        self.driver = driver

    def clickJewelryLink(self):
        self.driver.find_element(By.XPATH, self.jewelry_link_xpath).click()

    def clickAddToCart(self):
        self.driver.find_element(By.XPATH, self.addToCart_btn_xpath).click()

    def clickShoppingCart(self):
        self.driver.find_element(By.XPATH, self.shoppingcart_btn_xpath).click()