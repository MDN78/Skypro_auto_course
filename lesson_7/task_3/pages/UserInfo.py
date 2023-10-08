from pages.locators import UserInfo


class GetUserInfo:
    
    def __init__(self, driver):
        self._driver = driver
        
    def input_user_info(self, name, last_name, zip_code):
        first_name = self._driver.find_element(*UserInfo.first_name).send_keys(name)
        print("Input first name")
        last_name = self._driver.find_element(*UserInfo.last_name).send_keys(last_name)
        print("Input last name")
        zip_code = self._driver.find_element(*UserInfo.zip_code).send_keys(zip_code)
        print("Input Zip Code")
        button_continue = self._driver.find_element(*UserInfo.button_continue).click()
        print("Press the button 'continue'")