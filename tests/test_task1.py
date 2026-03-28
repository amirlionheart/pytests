import pytest
from tasks.task1 import check_age

@pytest.mark.parametrize("age, expected", [
    (17, 'Доступ запрещён'),
    (18, 'Доступ разрешён'),
    (0, 'Доступ запрещён'),
    (100, 'Доступ разрешён'),
    (-5, 'Доступ запрещён')
])

def test_check_age(age, expected):
    assert check_age(age) == expected
