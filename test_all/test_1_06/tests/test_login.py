import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
#Создадим тест для проверки обработки ошибок авторизации.
# Этот тест будет проверять, что при вводе неверных учетных данных URL не изменяется
# и что отображается корректное сообщение об ошибке.
def test_login_failure(l_page):
    l_page.navigate()
    l_page.login('noadmin', 'noadmin')
    assert l_page.error() == "Invalid credentials. Please try again."
#зашел на сайт, в аккаунт и там проверил что есть надпись внтури
@pytest.mark.parametrize("username, password",[
    ('user', "user"),
    ('admin', "admin"),
])
def testWelcomeText(l_page, d_page, username, password):
    l_page.navigate()
    l_page.login(username, password)
    d_page.AssertMassageWelcome(f"Welcome {username}")

