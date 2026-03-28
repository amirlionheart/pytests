import pytest
from tasks.task2 import check_auth

@pytest.mark.parametrize("login, password, expected", [
    ('admin', 'password', 'Добро пожаловать'),
    ('user', 'password', 'Доступ ограничен'),
    ('admin', '123', 'Доступ ограничен'),
    ('user', '123', 'Доступ ограничен'),
    ('ADMIN', 'password', 'Доступ ограничен'),
])

def test_check_auth(login, password, expected):
    assert check_auth(login, password) == expected