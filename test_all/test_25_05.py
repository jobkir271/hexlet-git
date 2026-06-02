from json import JSONDecodeError


def test_inventory(page):
    response = page.request.get('https://www.drom.ru/')
    print(response.status)
    try:
        print(response.json())
    except:
        print(response.text())