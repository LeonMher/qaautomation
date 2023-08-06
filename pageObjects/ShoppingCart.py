from selenium.webdriver.common.by import By
from Utilities.customLogger import MyLogger


class ShoppingCart:
    firstNameXpath = "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[2]/input"

    registerButtonXpath = "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[5]/button"
    shoppingCartClass = "itemquantity11231"

    productAddCart_Xpath = "/html/body/div[6]/div[3]/div/div/div/div/div[4]/div[2]/div[3]/div/div[2]/div[3]/div[2]/button[1]"

    cartQty_ClassName = "qty-input"

    logger = MyLogger()
    # driver.find_element_by_class_name
    logger.info("*************** Shopping Cart   *****************")
    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        self.driver.find_element(By.XPATH, self.productAddCart_Xpath).click()

    def theCart(self):
        cartItself = self.driver.find_element(By.CLASS_NAME, self.cartQty_ClassName)
        cart_count = cartItself.get_attribute('value')
        print(cart_count, ' cart count')
        # self.logger.info(cartItself)



