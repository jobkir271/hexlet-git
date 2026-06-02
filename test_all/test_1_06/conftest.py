
import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.fixture
def l_page(page):
    return LoginPage(page)
@pytest.fixture
def d_page(page):
    return DashboardPage(page)