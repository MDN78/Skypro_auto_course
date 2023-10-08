from selenium.webdriver.common.by import By
from pages.locators import ProductLocators, ProductPriceLocators, ProductButton

class AddProductCart:
    def __init__(self, driver):
        self._driver = driver
    
    def add_product_to_basket(self, name, price, button):
        product = self._driver.find_element(*name)
        value_product = product.text
    
        price_product = self._driver.find_element(*price)
        value_price_product = price_product.text.replace('$', '')
        
        select_product = self._driver.find_element(*button)
        select_product.click()
        print(f'Product "{value_product}", price: {value_price_product}, was added to basket')
    
    # def get_product_1(self):
    #     product_1 = self._driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
    #     value_product_1 = product_1.text

    #     price_product_1 = self._driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    #     value_price_product_1 = price_product_1.text.replace('$', '')

    #     select_product_1 = self._driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    #     select_product_1.click()
    #     print(f'First product "{value_product_1}", price: {value_price_product_1}, was added to basket')

    # def get_product_2(self):
    #     product_2 = self._driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div")
    #     value_product_2 = product_2.text

    #     price_product_2 = self._driver.find_element(By.XPATH, "//div[@class='inventory_list']//div[3]//div[@class='inventory_item_description']//div[@class='pricebar']//div[@class='inventory_item_price']")
    #     value_price_product_2 = price_product_2.text.replace('$', '')

    #     select_product_2 = self._driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    #     select_product_2.click()
    #     print(f'Second product "{value_product_2}", price: {value_price_product_2}, was added to basket')

    # def get_product_3(self):
    #     product_3 = self._driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div")
    #     value_product_3 = product_3.text

    #     price_product_3 = self._driver.find_element(By.XPATH, "//div[@class='inventory_list']//div[5]//div[@class='inventory_item_description']//div[@class='pricebar']//div[@class='inventory_item_price']")
    #     value_price_product_3 = price_product_3.text.replace('$', '')

    #     select_product_3 = self._driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
    #     select_product_3.click()
    #     print(f'Third product "{value_product_3}", price: {value_price_product_3}, was added to basket')