from playwright.sync_api import Page
from Pages.simple_page_2 import SimplePage2


def test_3(page: Page):
    simple_page_2 = SimplePage2(page)
    simple_page_2.open()
    simple_page_2.check_button_exists()

def test_4(page: Page):
    simple_page_2 = SimplePage2(page)
    simple_page_2.open()
    simple_page_2.click_button()
    simple_page_2.check_is_text_('Submitted')


