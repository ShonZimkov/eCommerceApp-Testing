import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen

class AddCustomer:

    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    btnAddnew_xpath = "/html[1]/body[1]/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"

    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstName_xpath = "FirstName"
    txtLastName_xpath = "LastName"
    rdMaleGender_xpath = "Gender_Male"
    rdFeMaleGender_xpath = "Gender_Female"
    txtDob_xpath = "DateOfBirth"
    txtCompanyName_xpath = "Company"

    txtcustomerRoles_xpath = "customer-info"
    lstitemAdministrators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    lstitemRegistered_xpath = "//*[@id='87a8a65f-25c2-4210-974e-fe6615f25cc3']"
    lstitemGuests_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstitemVendors_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    drpmgrOfVendor_xpath = "VendorId"
    txtAdminContent_xpath = "AdminComment"
    btnSave_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    # for getting to Edit Page
    btnEditCustomer_xpath = "//*[@id='customers-grid']/tbody/tr[1]/td[7]/a"
    logger = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()


    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstName_xpath).clear()
        self.driver.find_element(By.ID, self.txtFirstName_xpath).send_keys(fname)
    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_xpath).clear()
        self.driver.find_element(By.ID, self.txtLastName_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdMaleGender_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdFeMaleGender_xpath).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_xpath).click()

    def setDob(self, dob):
        self.driver.find_element(By.ID, self.txtDob_xpath).clear()
        self.driver.find_element(By.ID, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.ID, self.txtCompanyName_xpath).clear()
        self.driver.find_element(By.ID, self.txtCompanyName_xpath).send_keys(comname)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.ID, self.txtcustomerRoles_xpath).click()
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # here user can be registered or Guest , only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.ID, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element(By.ID, self.txtAdminContent_xpath).clear()
        self.driver.find_element(By.ID, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

    # for getting into Edit customer page
    def clickEditCustomer(self):
        self.driver.find_element(By.XPATH, self.btnEditCustomer_xpath).click()