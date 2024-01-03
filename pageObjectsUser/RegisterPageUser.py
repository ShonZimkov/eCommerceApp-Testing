import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class RegisterUser:
    # registration page elements and functions
    register_btn_xpath = "/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[1]/div[3]/button"
    rdMaleGender_id = "gender-male"
    rdFemaleGender_id = "gender-female"
    txtFirstName_id = "FirstName"
    txtLastName_id = "LastName"
    drpDobDay_name = "DateOfBirthDay"
    drpDobMonth_name = "DateOfBirthMonth"
    drpDobYear_name = "DateOfBirthYear"
    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtConfirmPassword_id = "ConfirmPassword"
    txtCompanyName_id = "Company"
    registerIN_btn_id = "register-button"

    def __init__(self, driver):
        self.driver = driver

    def clickOnRegister(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, self.register_btn_xpath).click()

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, firstName):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lastName)

    def setDob(self, d,m,y):
        day = Select(self.driver.find_element(By.NAME, self.drpDobDay_name))
        day.select_by_visible_text(d)
        month = Select(self.driver.find_element(By.NAME, self.drpDobMonth_name))
        month.select_by_visible_text(m)
        year = Select(self.driver.find_element(By.NAME, self.drpDobYear_name))
        year.select_by_visible_text(y)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setCompanyName(self, companyName):
        self.driver.find_element(By.ID, self.txtCompanyName_id).clear()
        self.driver.find_element(By.ID, self.txtCompanyName_id).send_keys(companyName)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtPassword_id).clear()
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(password)
        self.driver.find_element(By.ID, self.txtConfirmPassword_id).clear()
        self.driver.find_element(By.ID, self.txtConfirmPassword_id).send_keys(password)

    def clickOnRegisterIN(self):
        self.driver.find_element(By.ID, self.registerIN_btn_id).click()
