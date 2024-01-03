import configparser

config = configparser.RawConfigParser()
config.read('.\\Configuration\\config.ini')

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getUserLoginURL():
        url = config.get('common info', 'userloginURL')
        return url

    @staticmethod
    def getHomeURL():
        url = config.get('common info', 'homeURL')
        return url

    @staticmethod
    def getAddCustomer():
        addcust = []
        cust_password = config.get('add customer', 'cust_password')
        addcust.append(cust_password)
        cust_role = config.get('add customer', 'cust_role')
        addcust.append(cust_role)
        cust_vendor = config.get('add customer', 'cust_vendor')
        addcust.append(cust_vendor)
        cust_fname = config.get('add customer', 'cust_fname')
        addcust.append(cust_fname)
        cust_lname = config.get('add customer', 'cust_lname')
        addcust.append(cust_lname)
        cust_dob = config.get('add customer', 'cust_dob')
        addcust.append(cust_dob)
        cust_company = config.get('add customer', 'cust_company')
        addcust.append(cust_company)
        cust_admin_content = config.get('add customer', 'cust_admin_content')
        addcust.append(cust_admin_content)

        return addcust

    @staticmethod
    def getEditCustomer():
        editcust = []
        cust_password = config.get('edit customer', 'cust_password')
        editcust.append(cust_password)
        cust_role = config.get('edit customer', 'cust_role')
        editcust.append(cust_role)
        cust_vendor = config.get('edit customer', 'cust_vendor')
        editcust.append(cust_vendor)
        cust_fname = config.get('edit customer', 'cust_fname')
        editcust.append(cust_fname)
        cust_lname = config.get('edit customer', 'cust_lname')
        editcust.append(cust_lname)
        cust_dob = config.get('edit customer', 'cust_dob')
        editcust.append(cust_dob)
        cust_company = config.get('edit customer', 'cust_company')
        editcust.append(cust_company)
        cust_admin_content = config.get('edit customer', 'cust_admin_content')
        editcust.append(cust_admin_content)

        return editcust

    @staticmethod
    def getSearchEmail():
        email = config.get('search customer', 'search_email')
        return email

    @staticmethod
    def getSearchFirstName():
        fname = config.get('search customer', 'search_fname')
        return fname

    @staticmethod
    def getSearchLastName():
        lname = config.get('search customer', 'search_lname')
        return lname

    @staticmethod
    def getRegisterUser():
        register_user = []
        cust_gender = config.get('register user', 'cust_gender')
        register_user.append(cust_gender)
        cust_fname = config.get('register user', 'cust_fname')
        register_user.append(cust_fname)
        cust_lname = config.get('register user', 'cust_lname')
        register_user.append(cust_lname)
        cust_day = config.get('register user', 'cust_day')
        register_user.append(cust_day)
        cust_month = config.get('register user', 'cust_month')
        register_user.append(cust_month)
        cust_year = config.get('register user', 'cust_year')
        register_user.append(cust_year)
        cust_email = config.get('register user', 'cust_email')
        register_user.append(cust_email)
        cust_company = config.get('register user', 'cust_company')
        register_user.append(cust_company)
        cust_password = config.get('register user', 'cust_password')
        register_user.append(cust_password)

        return register_user

    @staticmethod
    def getUserUsername():
        username = config.get('user login', 'username')
        return username

    @staticmethod
    def getUserPassword():
        password = config.get('user login', 'password')
        return password

    @staticmethod
    def getBliingInfo():
        billing = []
        fname = config.get('billing', 'fname')
        billing.append(fname)
        lname = config.get('billing', 'lname')
        billing.append(lname)
        email = config.get('billing', 'email')
        billing.append(email)
        country = config.get('billing', 'country')
        billing.append(country)
        city = config.get('billing', 'city')
        billing.append(city)
        address = config.get('billing', 'address')
        billing.append(address)
        postal_code = config.get('billing', 'postal_code')
        billing.append(postal_code)
        phone_number = config.get('billing', 'phone_number')
        billing.append(phone_number)

        return billing

    @staticmethod
    def getCreditCard():
        credit_card = []
        card_holder = config.get('credit card', 'card_holder')
        credit_card.append(card_holder)
        card_number = config.get('credit card', 'card_number')
        credit_card.append(card_number)
        expiration_month = config.get('credit card', 'expiration_month')
        credit_card.append(expiration_month)
        expiration_year = config.get('credit card', 'expiration_year')
        credit_card.append(expiration_year)
        card_code = config.get('credit card', 'card_code')
        credit_card.append(card_code)

        return credit_card
