from selenium.webdriver.common.by import By

class MainPage:
    
    def __init__(self, driver, timeout=10):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(timeout)
        self._driver.maximize_window()
        
    def set_timer(self, time):
        timer = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        timer.clear()
        timer.send_keys(time)

    def summator(self):
        self._driver.find_element(By.XPATH, "//div[@class='keys']//span[1]").click()
        self._driver.find_element(By.XPATH, "//div[@class='keys']//span[4]").click()
        self._driver.find_element(By.XPATH, "//div[@class='keys']//span[2]").click()
        self._driver.find_element(By.XPATH, "//div[@class='keys']//span[15]").click()