from playwright.sync_api import  Page,expect,Dialog

def test_wiki(page: Page):
    page.goto("https://www.demoblaze.com/prod.html?idp_=1#")

    def dialogg(alert: Dialog):
        alert.accept()

    page.on('dialog', dialogg)
    page.get_by_text("Add to cart").click()
    page.wait_for_event('dialog')
    page.get_by_text("Home ").click()
    expect(page.locator("#itemc", has_text ="Laptops")).to_be_visible()