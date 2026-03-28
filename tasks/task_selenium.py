from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

YANDEX_AUTH_URL = "https://passport.yandex.ru/auth/"

def login_yandex(driver, login, password):
    """Попытка авторизации на Яндексе"""
    driver.get(YANDEX_AUTH_URL)
    time.sleep(2)  # ждём загрузку страницы

    # Ввод логина
    login_input = driver.find_element(By.ID, "passp-field-login")
    login_input.clear()
    login_input.send_keys(login)
    login_input.send_keys(Keys.ENTER)
    time.sleep(2)

    # Ввод пароля
    password_input = driver.find_element(By.ID, "passp-field-passwd")
    password_input.clear()
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(3)

    # Проверяем наличие ошибки
    errors = driver.find_elements(By.CLASS_NAME, "passp-form-field__error")
    if errors:
        return errors[0].text
    return "Вход успешен"