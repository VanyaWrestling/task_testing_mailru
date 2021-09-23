# Великанов Иван Вадимович vanya.velikanov.21.00@gmai.com
# https://github.com/VanyaWrestling/task_testing_mailru

import pytest

# Функция умножения
def multiplication(a, b):
    return a * b

# Функция деления
def division(a, b):
    return a / b

# Функция сложения значений словаря
def dct_return_sum_values_dict(dct):
    return dct.get('param1') + dct.get('param2') + dct.get('param3')

# Тест на сложение
@pytest.mark.parametrize("first_num, second_num, result", [(10, 2, 20), (15, -3, -45), (5, 10, 50), (4, 15, 60)])
def test_first_int(first_num, second_num, result):
    assert multiplication(first_num, second_num) == result

# Тест на ошибку при делении на 0
def test_second_int_devision_zero():
    with pytest.raises(ZeroDivisionError):
        division(5, 0)


dct = {
    'param1': 10,
    'param2': 20,
    'param3': 30
}

dct2 = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': 'val3',
}

dct3 = {
    'test1': 'value1',
    'test2': 'value2'
}

dct4 = dct3

# Тест на сложение значений словаря
def test_third_int():
    assert dct_return_sum_values_dict(dct) == 60

# Тест на тип словаря
def test_first_dict():
    assert type(dct) == dict

# Тест на неравенство ключей в словарях
def test_second_dict():
    assert dct.keys() != dct2.keys()

# Тест на копирование словаря
def test_third_dict():
    assert dct3 == dct4

# Тест на отчистку словаря
def test_fourth_dict():
    test_dict = {
        'param1': 1,
    }
    test_dict.clear()
    assert len(test_dict) == 0
