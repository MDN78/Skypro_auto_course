from selenium.webdriver.common.by import By
import allure

class AddProductCart:
    def __init__(self, driver):
        self._driver = driver
    
    @allure.step("Add product to basket")
    def add_product_to_basket(self, name: str, price: str, button: str) -> None:
        """Add product to cart"""
        product = self._driver.find_element(*name)
        value_product = product.text
    
        price_product = self._driver.find_element(*price)
        value_price_product = price_product.text.replace('$', '')
        
        select_product = self._driver.find_element(*button)
        select_product.click()
        allure.attach(value_product, 'Product', allure.attachment_type.TEXT)
        allure.attach(value_price_product, 'Price', allure.attachment_type.TEXT)
        print(f'Product "{value_product}", price: {value_price_product}, was added to basket')
    
    @allure.step("Checkout basket")
    def checkout(self, cart: str, checkout: str) -> None:
        """CHECKOUT"""
        cart_button = self._driver.find_element(*cart).click()
        print("Enter to basket")
        check = self._driver.find_element(*checkout)
        check.click()
        print("Click checkout")