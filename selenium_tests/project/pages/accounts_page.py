from selenium_tests.base_page import BasePage
from selenium_tests.elements.button import Button
from selenium_tests.elements.input import Input
from selenium_tests.elements.web_element import WebElement


class AccountsPage(BasePage):

    UNIQUE_ELEMENT_LOC = '_yuiResizeMonitor'
    SALES_LOC = '//a[@id="grouptab_0"]'
    ACCOUNTS_LOC = '//li[2]//span[2]//ul[1]//li[2]//a[1]'
    CREATE_ACCOUNTS_LOC = '//div[text()="Create Account"]'
    FIRST_NAME_ACCOUNTS_LOC = '//input[@id="name"]'
    PHONE_MOBILE_ACCOUNTS_LOC = '//input[@id="phone_office"]'
    SAVE_ACCOUNTS_LOC = '//table[@class="dcQuickEdit"]//input[@id="SAVE"]'
    ACCOUNTS_PAGE_LOC = '//div[@id="bootstrap-container"]'

    def __init__(self, driver):
        unique_element = WebElement(
            driver=driver,
            locator=self.UNIQUE_ELEMENT_LOC,
            description="Верхнее меню",
        )
        super().__init__(driver, unique_element)
        self.sales_input = Input(
            driver=self.driver,
            locator=self.SALES_LOC,
            description="Верхнее меню → Marketing",
        )
        self.accounts_input = Input(
            driver=self.driver,
            locator=self.ACCOUNTS_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент",
        )
        self.create_accounts_element = Button(
            driver=self.driver,
            locator=self.CREATE_ACCOUNTS_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Создать",
        )
        self.first_name_accounts = Button(
            driver=self.driver,
            locator=self.FIRST_NAME_ACCOUNTS_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Создать -> Имя",
        )
        self.phone_mobile_accounts = Button(
            driver=self.driver,
            locator=self.PHONE_MOBILE_ACCOUNTS_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Создать -> Имя -> Номер телефона",
        )
        self.save_accounts_button = Button(
            driver=self.driver,
            locator=self.SAVE_ACCOUNTS_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Создать -> Имя -> Номер телефона -> Сохранить",
        )
        self.accounts_page_button = Button(
            driver=self.driver,
            locator=self.ACCOUNTS_PAGE_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Создать -> Имя -> Номер телефона -> Сохранить -> Страница Kонтрагент",
        )

    def create_accounts(self):
        self.sales_input.click()
        self.accounts_input.click()
        self.create_accounts_element.click()

    def wait_account_page(self):
        self.accounts_page_button.wait_visibility()

