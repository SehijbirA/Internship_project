from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SETTINGS_BUTTON = (By.CSS_SELECTOR, "a.menu-button-block.w-inline-block[href='/settings']")

    def click_settings_button(self):
        self.click(*self.SETTINGS_BUTTON)