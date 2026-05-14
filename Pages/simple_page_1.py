from playwright.sync_api import expect
from Pages.base_page import BasePage

BUTTON = '#submit-id-submit'
ID_RESULT = '#result-text'

class SimplePage(BasePage):
    url = "https://www.qa-practice.com/elements/button/simple"

    def check_button_exists(self):
        button = self.page.locator(BUTTON)
        expect(button).to_be_visible()

    def click_button(self):
        self.page.locator(BUTTON).click()

    def check_is_text_(self,text):
        expect(self.page.locator(ID_RESULT)).to_have_text(text)