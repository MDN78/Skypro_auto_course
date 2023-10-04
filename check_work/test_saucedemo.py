from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'

def authorization():
    driver.get(base_url)
    driver.maximize_window()
    login_standard_user = "standard_user"
    password = "secret_sauce"
    user_name = driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(login_standard_user)
    print('Input login')
    password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
    print('Input password')
    button_login = driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    print('Click login button')

"""INFO products"""

def get_product_1():
    product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
    value_product_1 = product_1.text

    price_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_price_product_1 = price_product_1.text.replace('$', '')

    select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    select_product_1.click()
    print(f'First product "{value_product_1}", price: {value_price_product_1}, was added to basket')

def get_product_2():
    product_2 = driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div")
    value_product_2 = product_2.text

    price_product_2 = driver.find_element(By.XPATH, "//div[@class='inventory_list']//div[3]//div[@class='inventory_item_description']//div[@class='pricebar']//div[@class='inventory_item_price']")
    value_price_product_2 = price_product_2.text.replace('$', '')

    select_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    select_product_2.click()
    print(f'Second product "{value_product_2}", price: {value_price_product_2}, was added to basket')

def get_product_3():
    product_3 = driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div")
    value_product_3 = product_3.text

    price_product_3 = driver.find_element(By.XPATH, "//div[@class='inventory_list']//div[5]//div[@class='inventory_item_description']//div[@class='pricebar']//div[@class='inventory_item_price']")
    value_price_product_3 = price_product_3.text.replace('$', '')

    select_product_3 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
    select_product_3.click()
    print(f'Third product "{value_product_3}", price: {value_price_product_3}, was added to basket')

"""CHECKOUT"""
def checkout():
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    print("Enter to basket")
    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout.click()
    print("Click checkout")

"""User info"""

def input_user_info():
    first_name = driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys('Ivan')
    print("Input first name")
    last_name = driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys('Ivanov')
    print("Input last name")
    zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys(197197)
    print("Input Zip Code")
    button_continue = driver.find_element(By.XPATH, "//input[@id='continue']").click()
    print("Press the button 'continue'")
    
"""check price"""

def check_total_price():
    total_price = driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']")
    value_total_price = total_price.text.replace('Total: $', '')
    value_total_price_num = float(value_total_price)
    assert 58.29 == value_total_price_num, "Wrong total price!"
    print('Total summary price is good!')

"""finish process"""

def finish_process():
    finish = driver.find_element(By.XPATH, "//button[@id='finish']").click()
    back_home = driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()


def test_buy_products():
    authorization()
    get_product_1()
    get_product_2()
    get_product_3()
    checkout()
    input_user_info()
    check_total_price()
    finish_process()
    
    
