import pytest
from selenium import webdriver
from pageObjects.Login import Login
from Utilities.readProperties import ReadProperties
# from utilities.customLogger import LogGen
from Utilities.customLogger import MyLogger


class Test_Login_Logout:
    baseUrl = ReadProperties.getApplicationUrl()
    userEmail = "mtsatinyan2@gmail.com"
    userPassword = "kepler22bb"

    logger = MyLogger()
    logger.info("*************** Login and Logout   *****************")

    def testTitle(self):

        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        actualTitle = self.driver.title
        # Why do we close the webdriver, what if we don't actually close it

        if(actualTitle == "nopCommerce demo store. Login"):
            # whats assert for in python?
            self.driver.save_screenshot(".//screenshots//" + "TestCase_01.png")
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()


    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.userEmail)
        self.lp.setUserPassword(self.userPassword)
        self.lp.clickOnLogin()
        self.lp.clickOnLogout()
        actualTitle = self.driver.title

        self.driver.close()



        if(actualTitle == "nopCommerce demo store"):
            assert True
        else:
            assert False

  
