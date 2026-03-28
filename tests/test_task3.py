import pytest
from tasks.task3 import get_cost

@pytest.mark.parametrize("weight, expected", [
    (3, 'Стоимость доставки: 200 руб.'),
    (8, 'Стоимость доставки: 200 руб.'),
    (10, 'Стоимость доставки: 200 руб.'),
    (11, 'Стоимость доставки: 500 руб.'),
    (20, 'Стоимость доставки: 500 руб.'),
])

def test_get_cost(weight, expected):
    assert get_cost(weight) == expected
