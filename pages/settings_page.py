from pages.base_page import Page
from selenium.webdriver.common.by import By


class SettingsPage(Page):

    CONTACT_BUTTON = (By.CSS_SELECTOR, "a.page-setting-block.w-inline-block[href = '/contact-us']")

    def open_contact_us(self):
        self.click(*self.CONTACT_BUTTON)
