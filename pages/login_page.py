from pages.base_page.py import BasePage
from utils.locators import LoginPageLocators

class LoginPage(BasePage):
    def enter_username(self, username):
        self.send_keys(LoginPageLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)
