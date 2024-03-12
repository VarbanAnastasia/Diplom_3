import allure

from constants.urls import Urls
from pages.main_page import MainPage
#все тесты в хроме прошли, в фоксе нет

class TestMainPage:
    @allure.title("Проверка переключения на страницу заказов")
    def test_switch_to_order_history(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        main_page.current_url()
        main_page.url_to_be(Urls.ORDER_FEED)

        assert main_page.current_url() == Urls.ORDER_FEED

    @allure.title("Проверка переключения на страницу конструктора")
    def test_switch_to_constructor(self, driver, authentication):
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        main_page.go_to_constructor()
        main_page.url_to_be(Urls.MAIN_PAGE)

        assert main_page.current_url() == Urls.MAIN_PAGE

    @allure.title("Проверка открытия модального окна после клика на ингредиент")
    def test_modal__window_after_click_to_ingredient(self, driver, authentication):
        main_page = MainPage(driver)
        main_page.go_to_ingredient()

        assert main_page.wait_details(), "Детали об ингредиенте не появились"

    @allure.title("Проверка закрытия модального окна по нажатию на крестик")
    def test_close_modal_window(self, driver, authentication):
        main_page = MainPage(driver)
        main_page.go_to_ingredient()
        main_page.close_modal()

        assert main_page.closing_confirmation(), "Окно не закрылось по нажатию на крестик"

    @allure.title("Проверка измениния количества ингредиентов после добавления ингредиентов в корзину")
    def test_order_registration(self, driver, authentication):
        main_page = MainPage(driver)
        main_page.drag_and_drop()
        quantity = main_page.number_of_ingredients().text

        assert quantity == '2', "Количество ингредиентов не совпадает"

    @allure.title("Проверка создания заказа")
    def test_making_an_order(self, driver, authentication):
        main_page = MainPage(driver)
        main_page.drag_and_drop()
        main_page.make_an_order()

        assert main_page.confirmation_of_order(), "Заказ не сделан"

