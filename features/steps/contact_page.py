from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify the Contact us page opens')
def open_settings(context):
    context.app.contact_page.verify_contact_page_is_open()
    context.app.contact_page.verify_at_least_4_media_icons()
