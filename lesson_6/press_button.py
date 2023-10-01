from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = 'http://uitestingplayground.com/ajax'

driver.implicitly_wait(20)
driver.get(link)
driver.maximize_window()

button = driver.find_element(By.ID, "ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

driver.quit()
