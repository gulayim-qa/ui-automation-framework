import time
from selenium_tests.base_page import BasePage
from selenium_tests.elements.button import Button
from selenium_tests.elements.input import Input
from selenium_tests.elements.web_element import WebElement


class LinkLeadToCounterparty(BasePage):

    UNIQUE_ELEMENT_LOC = 'ygddfdiv'
    ACCOUNTS_LINK_LOC = '//span[@class="currentTab"]/a[text()="Accounts"]'
    CHOOSE_LEAD_LOC = '(//tr/td/a[contains(@href, "module=Accounts") and text()])[1]'
    PAGE_ACCOUNTS_LOC = '//div[@id="content"]'
    CREATE_LOC = '//span[@class="suitepicon suitepicon-action-caret subhover"]'
    SAVE_LOC = '//a[@id="account_leads_select_button"]'
    PAGE_LEAD_SEARCH_LOC = '//html[@lang="en_us"]'
    CHECKBOX_LOC = '(//input[@type="checkbox" and @class="checkbox"])[last()]'
    SELECT_LOC = '//input[@id="MassUpdate_select_button"]'



    def __init__(self, driver):
        unique_element = WebElement(
            driver=driver,
            locator=self.UNIQUE_ELEMENT_LOC,
            description="Верхнее меню",
        )
        super().__init__(driver, unique_element)
        self.accounts_link_input = Input(
            driver=self.driver,
            locator=self.ACCOUNTS_LINK_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент",
        )
        self.choose_lead_input = Input(
            driver=self.driver,
            locator=self.CHOOSE_LEAD_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Созданный лид",
        )
        self.page_accounts_button = Button(
            driver=self.driver,
            locator=self.PAGE_ACCOUNTS_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Созданный лид -> Страница контрагент",
        )
        self.create_button = Button(
            driver=self.driver,
            locator=self.CREATE_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Созданный лид -> Страница контрагент -> Создать",
        )
        self.save_button = Button(
            driver=self.driver,
            locator=self.SAVE_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Созданный лид -> Страница контрагент -> Создать -> Сохранить",
        )
        self.page_lead_search_button = Button(
            driver=self.driver,
            locator=self.PAGE_LEAD_SEARCH_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Созданный лид -> Страница контрагент -> Создать -> Сохранить -> Страница поиск лидов",
        )
        self.checkbox_input = Input(
            driver=self.driver,
            locator=self.CHECKBOX_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Созданный лид -> Страница контрагент -> Создать -> Сохранить -> Страница поиск лидов -> Галочка",
        )
        self.select_button = Button(
            driver=self.driver,
            locator=self.SELECT_LOC,
            description="Верхнее меню → Marketing -> Kонтрагент -> Созданный лид -> Страница контрагент -> Создать -> Сохранить -> Страница поиск лидов -> Галочка -> Выбрать",
        )

    def test_lead_and_counterparty_link(self):
        self.accounts_link_input.click()
        self.choose_lead_input.click()
        self.page_accounts_button.wait_visibility()
        self.create_button.click()
        self.save_button.click()
        self.page_lead_search_button.wait_visibility()
        self.checkbox_input.click()
        self.select_button.click()
        time.sleep(0.5)
