from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class HomePage:
    link_login_xpath = "//*[@id='masthead']/div[1]/div/div/div[2]/div/a[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnLogin(self):
        self.driver.find_element_by_xpath(self.link_login_xpath).click()
        