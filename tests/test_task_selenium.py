import os
import pytest
from selenium import webdriver
from tasks.task_selenium import login_yandex
from dotenv import load_dotenv

load_dotenv()
YANDEX_LOGIN = os.getenv("YANDEX_LOGIN")
YANDEX_PASSWORD = os.getenv("YANDEX_PASSWORD")

@pytest.mark.parametrize("login, password, expected", [
    ("invalid_login", "invalid_password", "Неверный логин или пароль"),
    (YANDEX_LOGIN, "wrong_password", "Неверный логин или пароль"),
    (YANDEX_LOGIN, YANDEX_PASSWORD, "Вход успешен")  # включайте только если безопасно
])
def test_login_yandex(login, password, expected):
    with webdriver.Chrome() as driver:  # браузер автоматически закроется
        driver.maximize_window()
        result = login_yandex(driver, login, password)

    assert expected in result