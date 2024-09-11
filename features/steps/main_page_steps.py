from behave import given, when, then
from time import sleep


@given('Open Reelly main page')
def open_reelly(context):
    context.app.main_page.open()


@given('Click Sign In')
def sign_in(context):
    context.app.main_page.signin()


@given('Log in to the page')
def log_in(context):
    context.app.main_page.login()


@when('Click on “off plan” at the left side menu')
def click_off_plan(context):
    #sleep(5)
    context.app.off_plan_page.click_off_plan_button()