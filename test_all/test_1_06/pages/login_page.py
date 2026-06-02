from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator(".btn.btn-primary.btn-block")
        self.error_massage = page.locator("#errorAlert")

    def navigate(self):
        self.page.goto("https://zimaev.github.io/pom/")

    def login(self, username:str, password:str)->str:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def error(self):
        return self.error_massage.inner_text()