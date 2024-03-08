import allure
from selenium.webdriver import ActionChains

from locators.main_page_locators import MainPageLocators
from pages.personal_account import PersonalAccount


class MainPage(PersonalAccount):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Переход на страницу ленты заказов")
    def go_to_order_feed(self):
        self.find_element_located_click(MainPageLocators.ORDER_FEED)

    @allure.step("Переход на страницу конструктора")
    def go_to_constructor(self):
        self.find_element_located_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход к ингредиенту")
    def go_to_ingredient(self):
        self.find_element_located_click(MainPageLocators.ONE_INGREDIENT)
        self.find_element_located(MainPageLocators.DETAILS_BUTTON)

    @allure.step("Ожидание деталей ингредиента")
    def wait_details(self):
        if self.find_element_located(MainPageLocators.DETAILS_BUTTON):
            return True

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.find_element_located_click(MainPageLocators.CLOSE_MODAL)

    @allure.step("Подтверждение закрытия модального окна")
    def closing_confirmation(self):
        if self.find_element_located(MainPageLocators.CLOSE_CONFIRMATION):
            return True

    @allure.step("Перетаскивание ингредиента")
    def drag_and_drop(self):
        drag = self.find_element_located(MainPageLocators.BURGER_INGREDIENT)
        drop = self.find_element_located(MainPageLocators.PLACE_FOR_ORDER)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    @allure.step("Получение количества ингредиентов")
    def number_of_ingredients(self):
        return self.find_element_located(MainPageLocators.NUMBER_OF_INGREDIENTS)

    @allure.step("Создание заказа")
    def make_an_order(self):
        self.find_element_located_click(MainPageLocators.MAKE_AN_ORDER_BUTTON)

    @allure.step("Подтверждение создания заказа")
    def confirmation_of_order(self):
        if self.find_element_located(MainPageLocators.CONFIRMATION_OF_MAKING_ORDER):
            return True

