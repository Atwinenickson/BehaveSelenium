from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    txt_username_id = "username"
    txt_password_id = "password"
    btn_login_xpath = "//*[@id='post-305']/div/div/div/div/div/form/p[2]/button"

    def __init__(self, driver):
        self.driver = driver

    
    def setusername(self, username):
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()