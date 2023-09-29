from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'http://the-internet.herokuapp.com/entry_ad'
driver.get(url)
driver.maximize_window()

element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-footer']")))
element.click()


time.sleep(2)
driver.close()
