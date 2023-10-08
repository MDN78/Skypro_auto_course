from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Asserts:
    def __init__(self, driver):
        self._driver = driver
        
    def assert_result(self):
        self._driver.current_url
        result = WebDriverWait(self._driver, 50).until(
            EC.text_to_be_present_in_element((By.XPATH, "//div[@class='screen']"), '15')
        )
        result_text = self._driver.find_element(By.XPATH, "//div[@class='screen']").text
        assert '15' == result_text, "Wrong result"