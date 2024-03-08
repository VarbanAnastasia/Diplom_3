import allure

from constants.urls import Urls
from pages.personal_account import PersonalAccount
#все тесты в хроме прошли, в фоксе нет


class TestPersonalAccount:

    @allure.title("Проверка переключения на страницу личного кабинета")
    def test_switch_to_personal_account(self, driver, authentication):
        personal_account = PersonalAccount(driver)
        personal_account.go_to_personal_account()
        personal_account.current_url()
        personal_account.url_to_be(Urls.PERSONAL_PAGE)

        assert personal_account.current_url() == Urls.PERSONAL_PAGE

    @allure.title("Проверка переключения на страницу истории заказов")
    def test_switch_to_order_history(self, driver, authentication):
        personal_account = PersonalAccount(driver)
        personal_account.go_to_personal_account()
        personal_account.go_to_order_history()
        personal_account.current_url()
        personal_account.url_to_be(Urls.ORDER_HISTORY)

        assert personal_account.current_url() == Urls.ORDER_HISTORY

    @allure.title("Проверка выхода")
    def test_exit_account(self, driver, authentication):
        personal_account = PersonalAccount(driver)
        personal_account.go_to_personal_account()
        personal_account.exit_account()
        personal_account.current_url()
        personal_account.url_to_be(Urls.LOGIN_PAGE)

        assert personal_account.current_url() == Urls.LOGIN_PAGE
