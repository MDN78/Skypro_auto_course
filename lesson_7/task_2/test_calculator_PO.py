from MainPage import MainPage
from selenium import webdriver
from asserts import Asserts
import allure

@allure.epic("Train site")
@allure.severity(severity_level='blocker')
@allure.title("Calculator")
def test_sum_result():
    driver = webdriver.Chrome()
    mp = MainPage(driver)
    with allure.step("Set timer"):
        mp.set_timer('45')
    with allure.step("Input dates"):
        mp.summator()
    
    with allure.step("Check result"):
        checking = Asserts(driver)
        checking.assert_result()
    
    driver.close()
