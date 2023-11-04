from pages.StartPage import StartPage
from pages.ProductsPage import AddProductCart
from pages.UserInfo import GetUserInfo
from pages.CheckoutPage import FinishPage
from selenium import webdriver
from pages.locators import ProductLocators, ProductPriceLocators, ProductButton, Checkout
import allure

@allure.epic("Internet shop Saucedemo")
@allure.severity(severity_level='critical')
@allure.story("Internet shop")
@allure.title("Smoke testing - buying process")
def test_buy_products():
    driver = webdriver.Chrome()
    
    with allure.step("Authorization"):
        auth = StartPage(driver)
        auth.authorization('standard_user', 'secret_sauce')
    
    add = AddProductCart(driver)
    
    with allure.step("add sauce_labs_backpack"):
        add.add_product_to_basket(
            ProductLocators.sauce_labs_backpack, 
            ProductPriceLocators.sauce_labs_backpack_price,
            ProductButton.sauce_labs_backpack_button
            )
    
    with allure.step("add sauce_labs_bolt_t_shirt"):
        add.add_product_to_basket(
            ProductLocators.sauce_labs_bolt_t_shirt,
            ProductPriceLocators.sauce_labs_bolt_t_shirt_price,
            ProductButton.sauce_labs_bolt_t_shirt_button
        )

    with allure.step("add sauce_labs_onesie"):
        add.add_product_to_basket(
            ProductLocators.sauce_labs_onesie,
            ProductPriceLocators.sauce_labs_onesie_price,
            ProductButton.sauce_labs_onesie_button
        )

    with allure.step("Checkout"):
        add.checkout(Checkout.cart, Checkout.checkout_button)
    
    #add user info
    with allure.step("add user info"):
        user = GetUserInfo(driver)
        user.input_user_info('Ivan', 'Ivanov', '345543')
    
    with allure.step("Check and finish"):
        finish = FinishPage(driver)
        finish.check_total_price(58.29)
        finish.finish_process()

    driver.close()