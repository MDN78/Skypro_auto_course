from selenium.webdriver.common.by import By
# from pages.locators import ProductLocators, ProductPriceLocators, ProductButton, Checkout

class AddProductCart:
    def __init__(self, driver):
        self._driver = driver
    """Add product to cart"""
    def add_product_to_basket(self, name, price, button):
        product = self._driver.find_element(*name)
        value_product = product.text
    
        price_product = self._driver.find_element(*price)
        value_price_product = price_product.text.replace('$', '')
        
        select_product = self._driver.find_element(*button)
        select_product.click()
        print(f'Product "{value_product}", price: {value_price_product}, was added to basket')
    
    """CHECKOUT"""
    def checkout(self, cart, checkout):
        cart_button = self._driver.find_element(*cart).click()
        print("Enter to basket")
        check = self._driver.find_element(*checkout)
        check.click()
        print("Click checkout")