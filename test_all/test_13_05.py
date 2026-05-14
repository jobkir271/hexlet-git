
from playwright.sync_api import Page,BrowserContext

def test_vkladka(page: Page, context: BrowserContext):
    page.goto("https://nomads.com/")
    with context.expect_page() as new_tab_event:
        page.get_by_alt_text("Get insured").click()
        new_tab = new_tab_event.value
    new_tab.get_by_role("link", name="Get covered now").first.click()

    #выше вкладки, ниже айфрейм разбор сайт для тренировок https://www.qa-practice.com/elements/iframe/iframe_page

def test_aiframe(page: Page):
    page.goto("https://www.qa-practice.com/elements/iframe/iframe_page")
    page.frame_locator("iframe").locator('.navbar-toggler-icon').click()

    #слектор он же дроп даун он же выпадающий всписок

def test_selector(page: Page):
    page.goto('https://www.qa-practice.com/elements/select/single_select')
    page.locator('#id_choose_language').select_option('Python')


