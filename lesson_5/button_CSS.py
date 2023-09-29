from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = 'http://uitestingplayground.com/classattr'
driver.get(url)
driver.maximize_window()


button = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(2)

alert = driver.switch_to.alert
alert.accept()

time.sleep(2)
driver.close()

