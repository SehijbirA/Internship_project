from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    USERNAME_TEXTBOX = (By.CSS_SELECTOR, "#email-2")
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR, "#field")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a.login-button.w-button")
    SIGN_IN_PAGE_URL = "https://soft.reelly.io/sign-in"
    USERNAME = "Sehij11@gmail.com"
    PASSWORD = "WindowFan32!"

    def open_sign_in_page(self):
        self.open_url(self.SIGN_IN_PAGE_URL)

    def sign_in_with_account(self):
        self.input(*self.USERNAME_TEXTBOX, text=self.USERNAME)
        self.input(*self.PASSWORD_TEXTBOX, text=self.PASSWORD)
        self.click(*self.CONTINUE_BUTTON)

