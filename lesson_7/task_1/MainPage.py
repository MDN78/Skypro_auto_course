from locators import MainPageLocators
from locators import Locators_for_checking_color
import allure


class MainPage:
        
    def __init__(self, driver, timeout=10):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.implicitly_wait(timeout)
        self._driver.maximize_window()
    
    @allure.step("Fill fields")
    def fill_fields(self):
        """ Methods for filling field forms"""
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
    
    @allure.step("Get color from field name")
    def check_field_first_name(self) -> str:
        """Check color of field name"""
        return self._driver.find_element(*Locators_for_checking_color.first_name).value_of_css_property('background-color')

    @allure.step("Get color from field last name")
    def check_field_last_name(self) -> str:
        """Check color of field last name"""
        return self._driver.find_element(*Locators_for_checking_color.last_name).value_of_css_property('background-color')

    @allure.step("Get color from field address")
    def check_field_address(self) -> str:
        """Check color of field address"""
        return self._driver.find_element(*Locators_for_checking_color.address).value_of_css_property('background-color')

    @allure.step("Get color from field phone")
    def check_field_phone(self) -> str:
        """Check color of field phone"""
        return self._driver.find_element(*Locators_for_checking_color.phone).value_of_css_property('background-color')

    @allure.step("Get color from field email")
    def check_field_email(self) -> str:
        """Check color of field email"""
        return self._driver.find_element(*Locators_for_checking_color.email).value_of_css_property('background-color')

    @allure.step("Get color from field zip code")
    def check_field_zip_code(self) -> str:
        """Check color of field zip code"""
        return self._driver.find_element(*Locators_for_checking_color.zip_code).value_of_css_property('background-color')

    @allure.step("Get color from field city")
    def check_field_city(self) -> str:
        """Check color of field city"""
        return self._driver.find_element(*Locators_for_checking_color.city).value_of_css_property('background-color')
    
    @allure.step("Get color from field country")
    def check_field_country(self) -> str:
        """Check color of field country"""
        return self._driver.find_element(*Locators_for_checking_color.country).value_of_css_property('background-color')

    @allure.step("Get color from field job position")
    def check_field_job_position(self) -> str:
        """Check color of field job position"""
        return self._driver.find_element(*Locators_for_checking_color.job_position).value_of_css_property('background-color')

    @allure.step("Get color from field company")
    def check_field_company(self) -> str:
        """Check color of field company"""
        return self._driver.find_element(*Locators_for_checking_color.company).value_of_css_property('background-color')
