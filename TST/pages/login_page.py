from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_FOR_REGISTRATION)
        input_email.send_keys(email)
        input_pwd = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_FOR_REGISTRATION)
        input_pwd.send_keys(password)
        repeat_pwd = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FOR_REGISTRATION)
        repeat_pwd.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Login link is incorrect"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
