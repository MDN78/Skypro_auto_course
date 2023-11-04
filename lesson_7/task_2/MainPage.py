from selenium.webdriver.common.by import By
import allure

class MainPage:
    
    @allure.step("Initialization driver")
    def __init__(self, driver, timeout=10):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(timeout)
        self._driver.maximize_window()
    
    @allure.step("Set timer {time}")
    def set_timer(self, time: str):
        """Set timer time"""
        timer = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        timer.clear()
        timer.send_keys(time)

    @allure.step("Input dates in calculator")
    def summator(self):
        """Input dates in calculator"""
        self._driver.find_element(By.XPATH, "//div[@class='keys']//span[1]").click()
        self._driver.find_element(By.XPATH, "//div[@class='keys']//span[4]").click()
        self._driver.find_element(By.XPATH, "//div[@class='keys']//span[2]").click()
        self._driver.find_element(By.XPATH, "//div[@class='keys']//span[15]").click()