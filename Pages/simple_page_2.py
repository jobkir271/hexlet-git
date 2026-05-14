from playwright.sync_api import expect
from Pages.base_page import BasePage

BUTTON = ".a-button"
ID_RESULT = 'Submitted'

class SimplePage2(BasePage):
    url = "https://www.qa-practice.com/elements/button/like_a_button"

    def check_button_exists(self):
        expect(self.page.locator(BUTTON)).to_be_visible()

    def click_button(self):
        self.page.locator(BUTTON).click()

    def check_is_text_(self,text):
        expect(self.page.get_by_text(ID_RESULT)).to_have_text(text)