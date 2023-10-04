from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'

def set_timer():
    driver.get(url)
    driver.maximize_window()
    timer = driver.find_element(By.CSS_SELECTOR, '#delay')
    timer.clear()
    timer.send_keys('45')

def summator():
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.XPATH, "//div[@class='keys']//span[1]").click()
    driver.find_element(By.XPATH, "//div[@class='keys']//span[4]").click()
    driver.find_element(By.XPATH, "//div[@class='keys']//span[2]").click()
    driver.find_element(By.XPATH, "//div[@class='keys']//span[15]").click()
   

def assert_result():
    driver.current_url
    result = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[@class='screen']"), '15')
    )
    result_text = driver.find_element(By.XPATH, "//div[@class='screen']").text
    assert '15' == result_text, "Wrong result"
    
def test_sum_result():
    set_timer()
    summator()
    assert_result()
