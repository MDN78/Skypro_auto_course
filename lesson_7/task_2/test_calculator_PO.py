from MainPage import MainPage
from selenium import webdriver
from asserts import Asserts

def test_sum_result():
    driver = webdriver.Chrome()
    mp = MainPage(driver)
    mp.set_timer('45')
    mp.summator()
    
    checking = Asserts(driver)
    checking.assert_result()
    
    driver.close()
