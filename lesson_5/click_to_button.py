from selenium import webdriver
import time
from selenium.webdriver.common.by import By




# select webdriver. Default driver - Chrome

# driver = webdriver.Firefox()
driver = webdriver.Chrome()


url = 'http://the-internet.herokuapp.com/add_remove_elements/'
driver.get(url)
driver.maximize_window()

spisok = []

for i in range(5):
    driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()
    locator = '//*[@id="elements"]/button[' + str(i + 1) + ']'
    spisok.append(driver.find_element(By.XPATH, locator).text)
    
print(len(spisok))

time.sleep(2)
driver.close()

