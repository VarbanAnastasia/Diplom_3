import allure

from constants.urls import Urls
from constants.constants import UserInfo
from locators.reset_password_locators import ResetPasswordLocators
from pages.reset_password import ResetPassword
#все тесты в хроме прошли, в фоксе нет


class TestResetPassword:
    @allure.title("Проверка переключения на страницу восстановления пароля")
    def test_switch_to_reset_password(self, driver):
        reset_password = ResetPassword(driver)
        reset_password.go_to_reset_password_page()
        reset_password.current_url()

        assert reset_password.current_url() == Urls.RESET_PAGE

    @allure.title("Проверка переключения на страницу подтверждения восстановления пароля")
    def test_reset_password(self, driver):
        reset_password = ResetPassword(driver)
        reset_password.go_to_reset_password_page()
        reset_password.reset_confirmation()
        reset_password.current_url()

        assert reset_password.current_url() == Urls.CONFIRMATION_RESET_PAGE

    @allure.title("Проверка восстановления пароля")
    def test_password_visibility(self, driver):
        reset_password = ResetPassword(driver)
        reset_password.go_to_reset_password_page()
        reset_password.reset_confirmation()
        reset_password.find_element_send_key(ResetPasswordLocators.PASSWORD_INPUT_IN_RESET_PAGE, UserInfo.USER_PASSWORD)
        reset_password.find_element_located_click(ResetPasswordLocators.EYE_BUTTON)

        assert reset_password.find_element_located(ResetPasswordLocators.PASSWORD_VISIBLE)
