from selenium.webdriver.common.by import By

class MainPageLocators:
    first_name = (By.XPATH, "//input[@name='first-name']")
    last_name = (By.XPATH, "//input[@name='last-name']")
    address = (By.XPATH, "//input[@name='address']")
    email = (By.XPATH, "//input[@name='e-mail']")
    phone = (By.XPATH, "//input[@name='phone']")
    zip_code = (By.XPATH, "//input[@name='zip-code']")
    city = (By.XPATH, "//input[@name='city']")
    country = (By.XPATH, "//input[@name='country']")
    job_position = (By.XPATH, "//input[@name='job-position']")
    company = (By.XPATH, "//input[@name='company']")
    button_submit = (By.XPATH, "//button[@class='btn btn-outline-primary mt-3']")
    
class Locators_for_checking_color:
    first_name = (By.XPATH, "//div[@id='first-name']")
    last_name = (By.XPATH, "//div[@id='last-name']")
    address = (By.XPATH, "//div[@id='address']")
    email = (By.XPATH, "//div[@id='e-mail']")
    phone = (By.XPATH, "//div[@id='phone']")
    zip_code = (By.XPATH, "//div[@id='zip-code']")
    city = (By.XPATH, "//div[@id='city']")
    country = (By.XPATH, "//div[@id='country']")
    job_position = (By.XPATH, "//div[@id='job-position']")
    company = (By.XPATH, "//div[@id='company']")
    button_submit = (By.XPATH, "//div[@id='job-position']")
    
class FieldColor:
    green = 'rgba(209, 231, 221, 1)'
    red = 'rgba(248, 215, 218, 1)'