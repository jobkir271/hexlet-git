from playwright.sync_api import  Page, expect

def test_1(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    pole_voda = page.locator('[placeholder="What needs to be done?"]')
    expect(pole_voda).to_have_value("")
    pole_voda.fill("1q")
    pole_voda.press('Enter')
    pole_voda.fill("2")
    pole_voda.press('Enter')
    zadacha = page.locator('li[data-testid="todo-item"]')
    expect(zadacha).to_have_count(2)
    # zad_1 = page.get_by_role("checkbox", name="Toggle Todo").first
    zad_1q = page.locator('li').filter(has_text="1й").locator('.toggle')
    zad_1q.check()
    expect(zad_1q).to_be_checked()
