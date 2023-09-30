from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = 'http://the-internet.herokuapp.com/inputs'
driver.get(url)
driver.maximize_window()

field = driver.find_element(By.XPATH, "//input[@type='number']").send_keys('1000')
time.sleep(1)
field = driver.find_element(By.XPATH, "//input[@type='number']").clear()
field = driver.find_element(By.XPATH, "//input[@type='number']").send_keys('999')


time.sleep(2)
driver.close()
