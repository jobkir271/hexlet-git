import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://stepik.org/course/128626/promo")
    page.get_by_role("link", name="Войти").click()
    page.get_by_role("textbox", name="E-mail").click()
    page.get_by_role("textbox", name="E-mail").fill("kir271")
    page.get_by_role("textbox", name="E-mail").press("Tab")
    page.get_by_role("textbox", name="Пароль").fill("2222")
    page.get_by_role("button", name="Войти").click()
    page.locator(".modal-dialog-top__close").click()
    page.get_by_role("button", name="Rubricator").click()
    page.locator("#ember1018").click()
    page.get_by_role("button", name="Русский").click()
    page.get_by_role("button", name="English", exact=True).click()
    page.get_by_text("Intermediate").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
