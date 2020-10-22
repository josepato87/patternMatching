import pytest

from src.utils import get_integer_from_input, get_elements_of_string, convert_list_to_string

def test_get_integer_from_input():
    inputs = '3\nsome-text'

    integer = get_integer_from_input(inputs)

    assert integer == 3


def test_get_elements_of_string():
    string = '*,*,c'
    separator = ','
    expected_elements = ['*', '*', 'c']

    result_list = get_elements_of_string(string, separator)

    assert result_list == expected_elements


def test_convert_list_to_string():
    list_elements = ['a', 'b', 'c']
    expected_string = 'a,b,c'

    assert convert_list_to_string(list_elements) == expected_string