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
mylogger = LogGen.logger()


@given('Launch the App')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager.install())
    mylogger.info("*******DRIVER INITIALIZED******")
    context.driver.get(baseURL)
    mylogger.info("********BROWSER LAUNCHED*******")


@when('enter login credentials')
def step_impl(context):
    mylogger.info("*****Passing Credentials******")
    global hpage
    global lpage

    hpage = HomePage(context.driver)
    hpage.clickOnLogin()
    lpage = LoginPage(context.driver)
    usr = ReadConfig.getUserName()
    pwd = ReadConfig.getPassword()
    time.sleep(5)
    lpage.setusername(usr)
    lpage.setpassword(pwd)
    mylogger.info("******Entered Credentials*******")


@then('click login')
def step_impl(context):
    lpage.clickOnLogin()
    mylogger.info("****Clicked Login Button")


@then('verify the page title and screenshot')
def step_impl(context):
    actual_title = context.driver.title
    expected_tile = "Login - Change 2 Automation"
    if actual_title == expected_tile:
        assert True
        context.driver.save_screenshot("Screenshots"+"Loginpage.png")
        allure.attach(context.driver.get_screenshot_as_png(), name="c2ta Login test", attachment_type=AttachmentType.PNG)
        mylogger.info("****Title matched******")
    else:
        mylogger.info("******Title not matched******")
        assert False
        time.sleep(5)


@then('close the App')
def step_impl(context):
    context.driver.close()
    mylogger.info("***Browser closed********")