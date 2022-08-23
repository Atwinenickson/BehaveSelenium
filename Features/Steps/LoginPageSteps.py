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


@given('Launch the App')
def step_impl(context):
    context.driver = webdriver.chrome(ChromeDriverManager.install())
    mylogger.info("*******DRIVER INITIALIZED******")
    context.driver.get(baseURL)
    mylogger.info("********BROWSER LAUNCHED*******")


@when('enter login credentials')
def step_impl(context):
    


@then('click login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then click login')


@then('verify the page title and screenshot')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify the page title and screenshot')


@then('close the App')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then close the App')