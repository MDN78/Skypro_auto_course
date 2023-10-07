from locators import MainPageLocators
from locators import Locators_for_checking_color


class MainPage:
        
    def __init__(self, driver, timeout=10):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.implicitly_wait(timeout)
        self._driver.maximize_window()
        
    def fill_fields(self):
        self._driver.find_element(*MainPageLocators.first_name).send_keys('Иван')
        self._driver.find_element(*MainPageLocators.last_name).send_keys('Петров')
        self._driver.find_element(*MainPageLocators.address).send_keys('Ленина, 55-3')
        self._driver.find_element(*MainPageLocators.email).send_keys('test@skypro.com')
        self._driver.find_element(*MainPageLocators.phone).send_keys('+79858999988787')
        self._driver.find_element(*MainPageLocators.zip_code).send_keys('')
        self._driver.find_element(*MainPageLocators.city).send_keys('Москва')
        self._driver.find_element(*MainPageLocators.country).send_keys('Россия')
        self._driver.find_element(*MainPageLocators.job_position).send_keys('QA')
        self._driver.find_element(*MainPageLocators.company).send_keys('SkyPro')
        button = self._driver.find_element(*MainPageLocators.button_submit)
        self._driver.execute_script("arguments[0].click();", button)
        
    def check_field_first_name(self):
        return self._driver.find_element(*Locators_for_checking_color.first_name).value_of_css_property('background-color')

    def check_field_last_name(self):
        return self._driver.find_element(*Locators_for_checking_color.last_name).value_of_css_property('background-color')

    def check_field_address(self):
        return self._driver.find_element(*Locators_for_checking_color.address).value_of_css_property('background-color')

    def check_field_phone(self):
        return self._driver.find_element(*Locators_for_checking_color.phone).value_of_css_property('background-color')

    def check_field_email(self):
        return self._driver.find_element(*Locators_for_checking_color.email).value_of_css_property('background-color')

    def check_field_zip_code(self):
        return self._driver.find_element(*Locators_for_checking_color.zip_code).value_of_css_property('background-color')
        
    def check_field_city(self):
        return self._driver.find_element(*Locators_for_checking_color.city).value_of_css_property('background-color')

    def check_field_country(self):
        return self._driver.find_element(*Locators_for_checking_color.country).value_of_css_property('background-color')

    def check_field_job_position(self):
        return self._driver.find_element(*Locators_for_checking_color.job_position).value_of_css_property('background-color')

    def check_field_company(self):
        return self._driver.find_element(*Locators_for_checking_color.company).value_of_css_property('background-color')
