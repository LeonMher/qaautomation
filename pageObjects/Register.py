from selenium.webdriver.common.by import By


class Register:
    firstNameXpath = "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[2]/input"
    lastNameXpath = "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[3]/input"
    emailXpath = "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[5]/input"
    passwordXpath = "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[4]/div[2]/div[1]/input"
    passwordRepeatXpath = "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[4]/div[2]/div[2]/input"

    registerButtonXpath = "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[5]/button"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self, firstNameValue):
        self.driver.find_element(By.XPATH, self.firstNameXpath).clear()
        self.driver.find_element(By.XPATH, self.firstNameXpath).send_keys(firstNameValue)

    def setLastName(self, lastNameValue):
        self.driver.find_element(By.XPATH, self.lastNameXpath).clear()
        self.driver.find_element(By.XPATH, self.lastNameXpath).send_keys(lastNameValue)

    def setEmail(self, userEmail):
        self.driver.find_element(By.XPATH, self.emailXpath).clear()
        self.driver.find_element(By.XPATH, self.emailXpath).send_keys(userEmail)

    def setPassword(self, userPassword):
        self.driver.find_element(By.XPATH, self.passwordXpath).clear()
        self.driver.find_element(By.XPATH, self.passwordXpath).send_keys(userPassword)

    def setConfirmPassword(self, userPassword):
        self.driver.find_element(By.XPATH, self.passwordRepeatXpath).clear()
        self.driver.find_element(By.XPATH, self.passwordRepeatXpath).send_keys(userPassword)



    def clickOnRegister(self):
        self.driver.find_element(By.XPATH, self.registerButtonXpath).click()
