import time
from selenium_tests.base_page import BasePage
from selenium_tests.elements.button import Button
from selenium_tests.elements.input import Input
from selenium_tests.elements.web_element import WebElement


class LoginPage(BasePage):
    UNIQUE_ELEMENT_LOC = "ajaxUI-history-field"
    USERNAME_FIELD_LOC = "//input[@id='user_name']"
    PASSWORD_FIELD_LOC = "//input[@id='username_password']"
    LOGIN_BUTTON_LOC = "//input[@id='bigbutton']"

    def __init__(self, driver):
        unique_element = WebElement(
            driver=driver,
            locator=self.UNIQUE_ELEMENT_LOC,
            description="Страница авторизации -> элемент ajaxUI-history-field",
        )
        super().__init__(driver, unique_element)
        self.login_input = Input(
            driver=driver,
            locator=self.USERNAME_FIELD_LOC,
            description='Страница авторизации -> Поле "Логин"',
        )
        self.password_input = Input(
            driver=driver,
            locator=self.PASSWORD_FIELD_LOC,
            description='Страница авторизации -> Поле "Пароль"',
        )
        self.login_button = Button(
            driver=driver,
            locator=self.LOGIN_BUTTON_LOC,
            description='Страница авторизации -> Кнопка "Войти"',
        )

    def authorization_click(self, login, password):
        self.login_input.send_keys(login)
        self.password_input.send_keys(password)
        self.login_button.click()
        time.sleep(0.5)