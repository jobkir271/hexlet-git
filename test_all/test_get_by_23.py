#тестовая практика филтров локаторов, нельзя вряд писать методы click.fill.press.

def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    loc_in = page.locator("a")
    print(f" Нашло: {loc_in.filter(has_text='Remo H. Jansen').count()}")
    loc_in.filter(has_text="Remo H. Jansen").click()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    x = page.get_by_placeholder("What needs to be done?")
    # x.click()
    x.fill('ЭЭЭЭЭ')
    x.press("Enter")