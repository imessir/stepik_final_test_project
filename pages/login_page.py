from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/accounts/login/" in self.browser.current_url, \
            f"Login url is incorrect, current url: '{self.browser.current_url}'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_INPUT), "No username input found in login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT), "No password input found in login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "No login button found in login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_USERNAME_INPUT), \
            "No username input found in registration form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_INPUT), \
            "No password input found in registration form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_INPUT), \
            "No confirm password input found in registration form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), \
            "No register button found in registration form"
