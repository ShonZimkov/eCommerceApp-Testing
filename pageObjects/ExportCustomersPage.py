from selenium.webdriver.common.by import By
import os

class ExportCustomers:
    drpExportBtn_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/div/button[2]"
    lstAllFoundXML_name = "exportxml-all"
    lstSelectedXML_id = "exportxml-selected"

    table_id = "customers-grid"
    tableRows_xpath = "//*[@id='customers-grid']/tbody/tr"


    def __init__(self, driver):
        self.driver = driver

    def ClickdrpExportBtn(self):
        self.driver.find_element(By.XPATH, self.drpExportBtn_xpath).click()

    def ClicklstAllFoundXML(self):
        self.driver.find_element(By.NAME, self.lstAllFoundXML_name).click()

    def ClicklstSelectedXML(self):
        self.driver.find_element(By.ID, self.lstSelectedXML_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def ClickSelectCustomer(self):
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.ID, self.table_id)
            table.find_element(By.XPATH, "//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[1]/input").click()
        return
