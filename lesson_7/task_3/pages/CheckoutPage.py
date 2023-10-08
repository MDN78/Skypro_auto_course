from selenium.webdriver.common.by import By

class FinishPage:    
    
    def __init__(self, driver):
        self._driver = driver
        
    """check price"""

    def check_total_price(self, price):
        total_price = self._driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']")
        value_total_price = total_price.text.replace('Total: $', '')
        value_total_price_num = float(value_total_price)
        assert price == value_total_price_num, "Wrong total price!"
        print('Total summary price is good!')

    """finish process"""

    def finish_process(self):
        finish = self._driver.find_element(By.XPATH, "//button[@id='finish']").click()
        back_home = self._driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()