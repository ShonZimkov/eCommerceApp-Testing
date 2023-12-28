from selenium.webdriver.common.by import By

class CatalogPage:

    catalog_lnk_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a"
    products_lnk_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a"
    categories_lnk_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[2]/a"
    manufacturers_lnk_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[3]/a"
    productReviews_lnk_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[4]/a"

    products_addBtn_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    products_saveBtn_name = "save"
    categories_addBtn_xpath = "/html/body/div[3]/div[1]/div[1]/div/a"
    categories_saveBtn_name = "save"
    manufacturerAddBtn_xpath = "/html/body/div[3]/div[1]/div[1]/div/a"
    manufacturerSaveBtn_name = "save"
    productReviewApproveBtn_id = "approve-selected"
    productReviewDisapproveBtn_id = "disapprove-selected"
    productReviewDeleteBtn_id = "delete-selected"
    productReviewDeleteConfirmationBtn_id = "delete-selected-action-confirmation-submit-button"

    def __init__(self, driver):
        self.driver = driver

    def clickCataloglink(self):
        self.driver.find_element(By.XPATH, self.catalog_lnk_xpath).click()

    def clickProductslink(self):
        self.driver.find_element(By.XPATH, self.products_lnk_xpath).click()

    def clickCategorieslink(self):
        self.driver.find_element(By.XPATH, self.categories_lnk_xpath).click()

    def clickManufacturerslink(self):
        self.driver.find_element(By.XPATH, self.manufacturers_lnk_xpath).click()

    def clickProductReviewslink(self):
        self.driver.find_element(By.XPATH, self.productReviews_lnk_xpath).click()

    def clickAddProduct(self):
        self.driver.find_element(By.XPATH, self.products_addBtn_xpath).click()

    def clickSaveProduct(self):
        self.driver.find_element(By.NAME, self.products_saveBtn_name).click()

    def clickAddCategory(self):
        self.driver.find_element(By.XPATH, self.categories_addBtn_xpath).click()

    def clickSaveCategory(self):
        self.driver.find_element(By.NAME, self.categories_saveBtn_name).click()

    def clickAddManufacturer(self):
        self.driver.find_element(By.XPATH, self.manufacturerAddBtn_xpath).click()

    def clickSaveManufacturer(self):
        self.driver.find_element(By.NAME, self.manufacturerSaveBtn_name).click()

    def clickReportsApproved(self):
        self.driver.find_element(By.ID, self.productReviewApproveBtn_id).click()

    def clickReportsDisapproved(self):
        self.driver.find_element(By.ID, self.productReviewDisapproveBtn_id).click()

    def clickReportsDeleted(self):
        self.driver.find_element(By.ID, self.productReviewDeleteBtn_id).click()

    def clickReportsDeletedConfirmation(self):
        self.driver.find_element(By.ID, self.productReviewDeleteConfirmationBtn_id).click()