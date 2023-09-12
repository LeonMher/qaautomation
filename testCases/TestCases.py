import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pageObjects.Login import Login
from Utilities.readProperties import ReadProperties
from Utilities.customLogger import MyLogger



class Test_Login_Logout:
    baseUrl = ReadProperties.getApplicationUrl()
    userEmail = "mtsatinyan10@gmail.com"
    userPassword = "kepler22bb"

    logger = MyLogger()
    logger.info("*************** Login and Logout   *****************")

    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    def testTitle(self):


        # self.driver = webdriver.Chrome()

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(self.baseUrl)
        actualTitle = self.driver.title

        if(actualTitle == "nopCommerce demo store. Login"):
            self.driver.save_screenshot(".//screenshots//" + "TestCase_01.png")
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()


    def test_login(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self)
        self.lp.setUserPassword(self)
        self.lp.clickOnLogin()
        self.lp.clickOnLogout()
        actualTitle = self.driver.title

        self.driver.close()



        if(actualTitle == "nopCommerce demo store"):
            assert True
        else:
            assert False

  
