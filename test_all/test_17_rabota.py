import re
from playwright.sync_api import Playwright, sync_playwright, expect
from typing import Union
def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")

class A:
    x = 1
    y = 2
class calculator:
    def divide(self, x : Union[int, float], y : Union[int, float]):
        if not isinstance(x, (int,float)) or not isinstance(y,(int,float)):
            raise TypeError('ошибка типа')
        if y == 0:
            raise ZeroDivisionError("на ноль не делим")
        return x / y

    def add (self, x : Union[int, float], y : Union[int, float]):
        return x + y