from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, './/a[@class="AppHeader_header__link__3D_hX" and @href="/account"] ')
    PASSWORD_INPUT = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']")
    PASSWORD_INPUT_ACTIVE = (By.CSS_SELECTOR, ".input__container .input_status_active")
    ORDER_HISTORY = (By.XPATH, './/a[@href="/account/order-history"]')
    EXIT_BUTTON = (By.CSS_SELECTOR, 'button.Account_button__14Yp3')

