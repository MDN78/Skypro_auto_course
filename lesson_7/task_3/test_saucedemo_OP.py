from pages.StartPage import StartPage
from pages.ProductsPage import AddProductCart
from selenium import webdriver
from pages.locators import ProductLocators, ProductPriceLocators, ProductButton
import time

def test_buy_products():
    driver = webdriver.Chrome()
    
    auth = StartPage(driver)
    auth.authorization('standard_user', 'secret_sauce')
    
    add = AddProductCart(driver)
    # add sauce_labs_backpack
    add.add_product_to_basket(
        ProductLocators.sauce_labs_backpack, 
        ProductPriceLocators.sauce_labs_backpack_price,
        ProductButton.sauce_labs_backpack_button
        )
    # add sauce_labs_bolt_t_shirt
    add.add_product_to_basket(
        ProductLocators.sauce_labs_bolt_t_shirt,
        ProductPriceLocators.sauce_labs_bolt_t_shirt_price,
        ProductButton.sauce_labs_bolt_t_shirt_button
    )
    
    # add sauce_labs_onesie
    add.add_product_to_basket(
        ProductLocators.sauce_labs_onesie,
        ProductPriceLocators.sauce_labs_onesie_price,
        ProductButton.sauce_labs_onesie_button
    )
    
    time.sleep(3)
    driver.close()