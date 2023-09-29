from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = 'http://uitestingplayground.com/dynamicid'
driver.get(url)
driver.maximize_window()

for i in range(3):
    blue_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
    driver.refresh()


time.sleep(2)
driver.close()
