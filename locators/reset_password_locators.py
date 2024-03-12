from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    RESET_PASSWORD_AT_MAIN = (By.XPATH, ".//a[@href='/forgot-password']")
    ENTRANCE_BUTTON_FROM_RESET = (By.CLASS_NAME, "Auth_link__1fOlj")
    MAIL_INPUT = (By.CLASS_NAME, "input__textfield")
    ENTRANCE_FROM_PERSONAL = (By.CLASS_NAME, "button_button_size_medium__3zxIa")
    ENTRANCE_FROM_MAIN = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                    "button_button_size_large__G21Vg']")
    CONFIRMATION_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")
    PASSWORD_INPUT_IN_RESET_PAGE = (By.CSS_SELECTOR, ".input_type_password .input__textfield ")
    EYE_BUTTON = (By.CSS_SELECTOR, "div.input__icon.input__icon-action > svg")
    PASSWORD_VISIBLE = (By.CLASS_NAME, "input_status_active")
