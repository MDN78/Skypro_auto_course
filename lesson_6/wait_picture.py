from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
link = 'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html'
driver.get(link)
driver.maximize_window()

picture = WebDriverWait(driver, 40).until(
    EC.element_to_be_clickable((By.ID, "award")) 
).get_attribute("src")

print(f"Attribute src is: \n{picture}")

driver.quit()