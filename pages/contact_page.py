from pages.base_page import Page
from selenium.webdriver.common.by import By


class ContactPage(Page):
    CONTACT_PAGE_URL = "https://soft.reelly.io/contact-us"
    SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, "div [class = 'community-cards'] img.img-social ")

    def verify_contact_page_is_open(self):
        self.verify_partial_url(self.CONTACT_PAGE_URL)

    def verify_at_least_4_media_icons(self):
        social_media_icons = self.find_elements(*self.SOCIAL_MEDIA_ICONS)
        assert len(social_media_icons) > 4, f"There are less than 4 Social Media Images"
