#постваить все чек боксы

def test_to_do(page):
    page.goto("https://zimaev.github.io/checks-radios/")
    checkbox = page.locator('input')
    for i in checkbox.all():
        i.click()
# по тексту рядом с чекбоксом
def test_text_checkbox(page):
    page.goto("https://zimaev.github.io/checks-radios/")
    page.locator('text=Checked switch checkbox input').check()

#выпадающие списки
def test_1(page):
    page.goto("https://zimaev.github.io/select/")
    page.select_option('#skills', value=["linux","docker"])

#Dragon and drop перетаскивание
def test_2(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")
#загрузка файлов
def test_3(page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files("#formFileLg", "02python.py")
#Скачивание файла
def test_4(page):
    page.goto('https://demoqa.com/upload-download')
    # Ловим скачивание
    with page.expect_download() as download_info:
        page.locator("#downloadButton").click()
    # Сохраняем
    download_info.value.save_as("file.pdf")

#Текст выводим
def test_5(page):
    page.goto('https://demoqa.com/webtables')
    x = page.locator("tbody")
    text = x.all_inner_texts()
    xClean = text.replace("\t", " ").replace("\n", " ")
    print(xClean)
#работа с другой вкладкой в тесте
def test_tabs(page):
    page.goto("https://zimaev.github.io/tabs/")

    # Ловим новую вкладку
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    # Работаем с новой вкладкой
    new_tab = tab.value
    assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"