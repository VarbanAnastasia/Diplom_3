import allure

from constants.urls import Urls
from constants.constants import UserInfo

from locators.reset_password_locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPassword(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_reset_password_page(self):
        self.find_element_located_click(ResetPasswordLocators.ENTRANCE_FROM_MAIN)
        self.find_element_located_click(ResetPasswordLocators.RESET_PASSWORD_AT_MAIN)

    @allure.step("Подтверждение восстановления пароля")
    def reset_confirmation(self):
        self.find_element_located_click(ResetPasswordLocators.MAIL_INPUT)
        self.find_element_send_key(ResetPasswordLocators.MAIL_INPUT, UserInfo.USER_MAIL)
        self.find_element_located_click(ResetPasswordLocators.CONFIRMATION_BUTTON)
        self.url_to_be(Urls.CONFIRMATION_RESET_PAGE)

