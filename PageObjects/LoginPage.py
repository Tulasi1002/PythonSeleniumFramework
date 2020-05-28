from selenium.webdriver.common.by import By


class LoginPage:
    usernameBttn = (By.CSS_SELECTOR, "input[class='_2zrpKA _1dBPDZ']")
    passwordBttn = (By.CSS_SELECTOR, "input[type='password']")
    loginBttn = (By.XPATH, "//button[@type='submit']/span[.='Login']")

    def __init__(self, driver):
        self.driver = driver

    def findusernameBttn(self):
        return self.driver.find_element(*LoginPage.usernameBttn)

    def findpasswordBttn(self):
        return self.driver.find_element(*LoginPage.passwordBttn)

    def findloginBttn(self):
        return self.driver.find_element(*LoginPage.loginBttn)