from selenium.webdriver.common.by import By


class Login:
    login_input_id = "Email"
    password_input_id = "Password"
    login_button_xpath = "/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button"
    logout_button_xpath = "/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.login_input_id).clear()
        self.driver.find_element(By.ID, self.login_input_id).send_keys(username)

    def setUserPassword(self, password):
        self.driver.find_element(By.ID, self.password_input_id).clear()
        self.driver.find_element(By.ID, self.password_input_id).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def clickOnLogout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()