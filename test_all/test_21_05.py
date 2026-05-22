from idlelib.rpc import request_queue

from playwright.sync_api import Page

def test_perehvat(page: Page):

    page.goto("https://httpbin.org/forms/post")
    page.locator('input[name="custname"]').fill('morozov@gmail.com')
    page.get_by_role('button', name='Submit order').click()
    # page.route('requeste', lambda requeste_: requeste.method, requeste.url)

