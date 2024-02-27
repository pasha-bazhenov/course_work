from functions.funcs import last_executed_operation, sort_by_date
from classes.class_operation import Operation

# Переменная для test_last_executed_operation.
test_executed = [
    {'state': 'EXECUTED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},
    {'state': 'EXECUTED'},
    {'state': 'EXECUTED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},]


def test_last_executed_operation():
    """Проверка последних 5ти EXECUTED операций."""
    assert last_executed_operation(test_executed) == [
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},]


# Переменная для test_sort_by_date.
test_date = [
    {'date': '12'},
    {'date': '14'},
    {'date': '1'},
    {'date': '17'},]


def test_sort_by_date():
    """Проверка сортировки по дате"""
    assert sort_by_date(test_date) == [
        {'date': '17'},
        {'date': '14'},
        {'date': '12'},
        {'date': '1'},]


# Переменные для проверки класса Operation.
from_ = {'from': 'Visa Classic 2842878893689012',
         'to': 'Счет 35158586384610753655'}
to_ = {'to': 'Счет 90424923579946435907'}
date_ = {'date': '2019-12-08T22:46:21.935582',
         'description': 'Открытие вклада'}
amount_ = {'operationAmount': {'amount': '41096.24',
                               'currency': {'name': 'USD',
                                            'code': 'USD'}}}


def test_class():
    """Проверка методов класса Operation."""
    assert Operation(from_).from_to() == "Visa Classic  2842 87** **** 9012 -> Счет **3655"
    assert Operation(to_).from_to() == "Счет **5907"
    assert Operation(date_).date() == "08.12.2019 Открытие вклада"
    assert Operation(amount_).amount() == "41096.24 USD"