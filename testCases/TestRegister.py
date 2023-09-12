import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
from pageObjects.Register import Register
from pageObjects.Login import Login
from Utilities.readProperties import ReadProperties
from Utilities.customLogger import MyLogger


class Test_Register:
    baseUrl = ReadProperties.getApplicationRegisterUrl()
    userFirstName = "Mher"
    userLastName = "Tsatinyan"
    userEmail = "mtsatinyan12@gmail.com"


    userPassword = "kepler22bb"

    logger = MyLogger()
    logger.info("*************** Register   *****************")



    def test_register(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        actualTitle = self.driver.title


        self.lp = Register(self.driver)

        self.lp.setFirstName(self.userFirstName)
        self.lp.setLastName(self.userLastName)
        self.lp.setEmail(self.userEmail)
        self.lp.setPassword(self.userPassword)
        self.lp.setConfirmPassword(self.userPassword)

        self.lp.clickOnRegister()

        wait = WebDriverWait(self.driver, 10)
        # Wait for the title to be present and not empty
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "title")))
        print(f"Actual Title: {actualTitle}")

        time.sleep(5)
        if actualTitle == "nopCommerce demo store. Register":

            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()






