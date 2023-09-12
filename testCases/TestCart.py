from time import sleep

import pytest
from selenium import webdriver
from pageObjects.ShoppingCart import ShoppingCart
from pageObjects.Login import Login
from Utilities.readProperties import ReadProperties
from Utilities.customLogger import MyLogger


class Test_Cart:
    baseUrl = ReadProperties.getApplicationUrl()

    cartUrl = ReadProperties.getApplicationCartUrl()

    userEmail = "mtsatinyan10@gmail.com"

    userPassword = "kepler22bb"

    logger = MyLogger()
    logger.info("*************** Test Cart Start   *****************")

    def test_login_cart(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)

        # Login
        self.login = Login(self.driver)

        self.login.setUserName(self.userEmail)
        self.login.setUserPassword(self.userPassword)
        self.login.clickOnLogin()

        sleep(4)
        # Shopping
        self.lp = ShoppingCart(self.driver)
        self.lp.addToCart()

        sleep(2)

        self.driver.get(self.cartUrl)

        sleep(3)

        self.lp.theCart()





