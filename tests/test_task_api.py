import os
import pytest
from dotenv import load_dotenv
from tasks.task_api import create_folder, delete_folder

load_dotenv()
TOKEN = os.getenv("TOKEN")


# Позитивный тест: создание новой папки
@pytest.mark.parametrize("folder_name, expected_status", [
    ("test_folder_pytest_1", 201),
])
def test_create_folder_positive(folder_name, expected_status):
    # Чистим папку перед тестом
    delete_folder(folder_name, TOKEN)

    response = create_folder(folder_name, TOKEN)
    assert response.status_code == expected_status, f"Ожидался {expected_status}, но получили {response.status_code}"

    # Удаляем после теста
    delete_folder(folder_name, TOKEN)


# Негативный тест: папка уже существует
@pytest.mark.parametrize("folder_name, expected_status", [
    ("test_folder_pytest_2", 409),
])
def test_create_folder_existing(folder_name, expected_status):
    # Создаём папку один раз
    create_folder(folder_name, TOKEN)

    # Пытаемся создать снова
    response = create_folder(folder_name, TOKEN)
    assert response.status_code == expected_status, f"Ожидался {expected_status}, но получили {response.status_code}"

    # Удаляем после теста
    delete_folder(folder_name, TOKEN)


# Негативный тест: неверный токен
def test_create_folder_invalid_token():
    folder_name = "test_folder_invalid_token"
    invalid_token = "invalid_token_12345"
    response = create_folder(folder_name, invalid_token)
    assert response.status_code == 401, f"Ожидался 401, но получили {response.status_code}"