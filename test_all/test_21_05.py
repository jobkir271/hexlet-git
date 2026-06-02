# from idlelib.rpc import request_queue
#
from playwright.sync_api import Page
#
# def test_perehvat(page: Page):
#     page.route("**/post", lambda route: route.continue_(post_data='custname=xd'))
#     # page.route("**/post", lambda route: route.continue_(post_data='custname=morozov@gmail.com'))
#     page.goto("https://httpbin.org/forms/post")
#     page.locator('input[name="custname"]').fill('morozov@gmail.com')
#     page.get_by_role('button', name='Submit order').click()

#выше подмена при отправки, ниже подмена инфы которая приходит

from playwright.sync_api import Page

def test_my_mock(page: Page):
    page.route("**/todos/1", lambda route: route.fulfill(json={"title": "мое"}))
    page.goto("https://jsonplaceholder.typicode.com/todos/1")


