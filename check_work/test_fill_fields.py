import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
url = 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'


# locators
first_name = "//input[@name='first-name']"
last_name = "//input[@name='last-name']"
address = "//input[@name='address']"
email = "//input[@name='e-mail']"
phone = "//input[@name='phone']"
zip_code = "//input[@name='zip-code']"
city = "//input[@name='city']"
country = "//input[@name='country']"
job_position = "//input[@name='job-position']"
company = "//input[@name='company']"
button_submit = "//button[@class='btn btn-outline-primary mt-3']"



def fill_fields():
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.XPATH, first_name).send_keys('Иван')
    driver.find_element(By.XPATH, last_name).send_keys('Петров')
    driver.find_element(By.XPATH, address).send_keys('Ленина, 55-3')
    driver.find_element(By.XPATH, email).send_keys('test@skypro.com')
    driver.find_element(By.XPATH, phone).send_keys('+79858999988787')
    driver.find_element(By.XPATH, zip_code).send_keys('')
    driver.find_element(By.XPATH, city).send_keys('Москва')
    driver.find_element(By.XPATH, country).send_keys('Россия')
    driver.find_element(By.XPATH, job_position).send_keys('QA')
    driver.find_element(By.XPATH, company).send_keys('SkyPro')
    button = driver.find_element(By.XPATH, button_submit)
    driver.execute_script("arguments[0].click();", button)

def check_field_first_name():
    return driver.find_element(By.XPATH, "//div[@id='first-name']").value_of_css_property('background-color')

def check_field_last_name():
    return driver.find_element(By.XPATH, "//div[@id='last-name']").value_of_css_property('background-color')

def check_field_address():
    return driver.find_element(By.XPATH, "//div[@id='address']").value_of_css_property('background-color')

def check_field_phone():
    return driver.find_element(By.XPATH, "//div[@id='phone']").value_of_css_property('background-color')

def check_field_email():
    return driver.find_element(By.XPATH, "//div[@id='e-mail']").value_of_css_property('background-color')

def check_field_zip_code():
    return driver.find_element(By.XPATH, "//div[@id='zip-code']").value_of_css_property('background-color')
    
def check_field_city():
    return driver.find_element(By.XPATH, "//div[@id='city']").value_of_css_property('background-color')

def check_field_country():
    return driver.find_element(By.XPATH, "//div[@id='country']").value_of_css_property('background-color')

def check_field_job_position():
    return driver.find_element(By.XPATH, "//div[@id='job-position']").value_of_css_property('background-color')

def check_field_company():
    return driver.find_element(By.XPATH, "//div[@id='company']").value_of_css_property('background-color')

def check_field_job_position():
    return driver.find_element(By.XPATH, "//div[@id='job-position']").value_of_css_property('background-color')

def assert_background_color(color, result):
    assert color == result, "wrong color"


def test_check_authorization_form():
    fill_fields()
    assert_background_color(check_field_first_name(), 'rgba(209, 231, 221, 1)')
    assert_background_color(check_field_last_name(), 'rgba(209, 231, 221, 1)')
    assert_background_color(check_field_address(), 'rgba(209, 231, 221, 1)')
    assert_background_color(check_field_email(), 'rgba(209, 231, 221, 1)')
    assert_background_color(check_field_phone(), 'rgba(209, 231, 221, 1)')
    assert_background_color(check_field_zip_code(), 'rgba(248, 215, 218, 1)')
    assert_background_color(check_field_city(), 'rgba(209, 231, 221, 1)')
    assert_background_color(check_field_country(), 'rgba(209, 231, 221, 1)')
    assert_background_color(check_field_job_position(), 'rgba(209, 231, 221, 1)')
    assert_background_color(check_field_company(), 'rgba(209, 231, 221, 1)')
    
    
