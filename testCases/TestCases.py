import pytest
from selenium import webdriver
from pageObjects.Login import Login
from Utilities.readProperties import ReadProperties
# from utilities.customLogger import LogGen
from Utilities.customLogger import MyLogger


class TestCase_01:
    baseUrl = ReadProperties.getApplicationUrl()
    userEmail = "99.p3rc3n7@gmail.com"
    userPassword = "kepler22bb"

    logger = MyLogger()
    logger.info("*************** TestCase_01  *****************")

    def testTitle(self):
        self.logger.info("*************** Test_001_Login *****************")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        actualTitle = self.driver.title
        # Why do we close the webdriver, what if we don't actually close it

        if(actualTitle == "nopCommerce demo store. Login"):
            # whats assert for in python?
            self.logger.info("*************** Test passed *****************")
            self.driver.save_screenshot(".//screenshots//" + "TestCase_01.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*************** TestCase_01  *****************")
            assert False
            self.driver.close()


    # def test_login(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(self.baseUrl)
    #     self.lp = Login(self.driver)
    #     self.lp.setUserName(self.userEmail)
    #     self.lp.setUserPassword(self.userPassword)
    #     self.lp.clickOnLogin()
    #     actualTitle = self.driver.title
    #
    #     self.driver.close()
    #
    #
    #
    #     if(actualTitle == "nopCommerce demo store"):
    #         assert True
    #     else:
    #         assert False
