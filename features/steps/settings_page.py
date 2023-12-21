from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Click on Contact us option')
def open_settings(context):
    context.app.settings_page.open_contact_us()
