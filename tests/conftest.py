import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.personal_account import PersonalAccount


@allure.step('Открываем браузер')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.get("https://stellarburgers.nomoreparties.site/")

    yield driver
    driver.quit()

@allure.step("Авторизация")
@pytest.fixture
def authentication(driver):
    pa = PersonalAccount(driver)
    pa.authenticate()
