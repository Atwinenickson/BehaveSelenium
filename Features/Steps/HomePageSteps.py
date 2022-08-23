import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Homepage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readproperty import ReadConfig
import time

baseURL = ReadConfig.getUrl()
mylogger = LogGen.loggen()


@given('Launch the browser')
def step_impl(context):
    context.driver = webdriver.chrome(ChromeDriverManager.install())
    mylogger.info("*******DRIVER INITIALIZED******")
    context.driver.get(baseURL)
    mylogger.info("********BROWSER LAUNCHED*******")



@then('verify the page title')
def step_impl(context):
    actual_title = context.driver.title
    expected_tile = "Change 2 Automatation -Change 2 Automation"
    if actual_title==expected_tile:
        assert True
        mylogger.info("******Title Matched*******")
    else:
        mylogger.info("*****Title not matched******")
        assert False
        time.sleep(5)


@then('close the browser')
def step_impl(context):
    context.driver.close()
    mylogger.info("****Browser closed******")

 