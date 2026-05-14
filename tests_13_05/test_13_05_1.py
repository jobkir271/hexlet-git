from playwright.sync_api import Page
from Pages.simple_page_1 import SimplePage

def test_1(page: Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.check_button_exists()

def test_2(page: Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.click_button()
    simple_page.check_is_text_('Submitted')


