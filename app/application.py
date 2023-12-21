from pages.base_page import Page
from pages.sign_in_page import SignInPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.contact_page import ContactPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.sign_in_page = SignInPage(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.contact_page = ContactPage(driver)