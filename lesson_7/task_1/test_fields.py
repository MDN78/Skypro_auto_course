from MainPage import MainPage
from selenium import webdriver
from asserts import Asserts
from locators import FieldColor

def test_check_authorization_form():
    driver = webdriver.Chrome()
    
    main_page = MainPage(driver)
    main_page.fill_fields()
    
    Asserts(main_page.check_field_first_name(), FieldColor.green)
    Asserts(main_page.check_field_last_name(), FieldColor.green)
    Asserts(main_page.check_field_address(), FieldColor.green)
    Asserts(main_page.check_field_email(), FieldColor.green)
    Asserts(main_page.check_field_phone(), FieldColor.green)
    Asserts(main_page.check_field_zip_code(), FieldColor.red)
    Asserts(main_page.check_field_city(), FieldColor.green)
    Asserts(main_page.check_field_country(), FieldColor.green)
    Asserts(main_page.check_field_job_position(), FieldColor.green)
    Asserts(main_page.check_field_company(), FieldColor.green)
    
    driver.close()
    