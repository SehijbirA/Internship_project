from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the Sign In page')
def open_main_page(context):
    context.app.sign_in_page.open_sign_in_page()
    sleep(5)


@then('Log in to the Sign In page')
def log_in_from_sign_in_page(context):
    context.app.sign_in_page.sign_in_with_account()
