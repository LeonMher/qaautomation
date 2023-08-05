import pytest
from selenium import webdriver
from pageObjects.Register import Register
from Utilities.readProperties import ReadProperties
# from utilities.customLogger import LogGen
from Utilities.customLogger import MyLogger


class Test_Register:
    baseUrl = ReadProperties.getApplicationRegisterUrl()
    userFirstName = "Mher"
    userLastName = "Tsatinyan"
    userEmail = "mtsatinyan2@gmail.com"


    userPassword = "kepler22bb"

    logger = MyLogger()
    logger.info("*************** Register   *****************")

    def testTitle(self):

        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        actualTitle = self.driver.title
        # Why do we close the webdriver, what if we don't actually close it

        if (actualTitle == "nopCommerce demo store. Register"):

            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()

    def test_login(self):
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

        if (actualTitle == "nopCommerce demo store. Register"):

            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()



