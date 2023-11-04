from selenium.webdriver.common.by import By


class ProductLocators:
    """Items locators"""
    sauce_labs_backpack = (By.XPATH, "//a[@id='item_4_title_link']")
    sauce_labs_bolt_t_shirt = (By.XPATH, "//*[@id='item_1_title_link']/div")
    sauce_labs_onesie = (By.XPATH, "//*[@id='item_2_title_link']/div")
    

class ProductPriceLocators:
    """Product price locators"""
    sauce_labs_backpack_price = (By.XPATH, "//div[@class='inventory_item_price']")
    sauce_labs_bolt_t_shirt_price = (By.XPATH, "//div[@class='inventory_list']//div[3]//div[@class='inventory_item_description']//div[@class='pricebar']//div[@class='inventory_item_price']")
    sauce_labs_onesie_price = (By.XPATH, "//div[@class='inventory_list']//div[5]//div[@class='inventory_item_description']//div[@class='pricebar']//div[@class='inventory_item_price']")

class ProductButton:
    """Product button locators - add to basket"""
    sauce_labs_backpack_button = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    sauce_labs_bolt_t_shirt_button = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    sauce_labs_onesie_button = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
    
class Checkout:
    """Button locators checkout"""
    cart = (By.XPATH, "//a[@class='shopping_cart_link']")
    checkout_button = (By.XPATH, "//button[@id='checkout']")

class UserInfo:
    """User info locators"""
    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    zip_code = (By.XPATH, "//input[@id='postal-code']")
    button_continue = (By.XPATH, "//input[@id='continue']")
    
