from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Click on settings option')
def open_settings(context):
    context.app.main_page.click_settings_button()


