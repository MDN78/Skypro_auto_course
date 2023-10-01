from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
link = 'http://uitestingplayground.com/textinput'
driver.get(link)
driver.maximize_window()

SkyPro_name = driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")
press_button = driver.find_element(By.ID, "updatingButton").click()

text_button = WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )

print(driver.find_element(By.ID, "updatingButton").text)

driver.quit()

