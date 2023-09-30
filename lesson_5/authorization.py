from selenium import webdriver
import time
from selenium.webdriver.common.by import By



# select webdriver. Default driver - Chrome

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
url = 'http://the-internet.herokuapp.com/login'
driver.get(url)
driver.maximize_window()

username = driver.find_element(By.ID, "username").send_keys("tomsmith")
password = driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.XPATH, "//button[@class='radius']").click()


time.sleep(2)
driver.close()