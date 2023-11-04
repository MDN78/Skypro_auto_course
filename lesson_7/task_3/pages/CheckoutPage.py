from selenium.webdriver.common.by import By
import allure

class FinishPage:    
    
    def __init__(self, driver: str):
        self._driver = driver
    
    @allure.step("Check total price: {price}")
    def check_total_price(self, price: float) -> bool:
        """check price"""
        total_price = self._driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']")
        value_total_price = total_price.text.replace('Total: $', '')
        value_total_price_num = float(value_total_price)
        assert price == value_total_price_num, "Wrong total price!"
        print('Total summary price is good!')

    @allure.step("Back to main page")
    def finish_process(self) -> None:
        """finish process"""
        finish = self._driver.find_element(By.XPATH, "//button[@id='finish']").click()
        back_home = self._driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()