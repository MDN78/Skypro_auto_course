from selenium.webdriver.common.by import By
import allure

class StartPage:
    
    def __init__(self, driver, timeout=10):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(timeout)
        self._driver.maximize_window()
    
    @allure.step("Authorization {user_name} : {password}")
    def authorization(self, user_name: str, password: str) -> None:
        """Method for authorization user"""
        user_name = self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(user_name)
        print('Input login')
        password = self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        print('Input password')
        button_login = self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        print('Click login button')
