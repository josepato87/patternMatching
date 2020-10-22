from itertools import islice

PATTERN_SEPARATOR = ','


def get_integer_from_input(inputs):
    return int(list((islice(inputs, 1)))[0])


def get_elements_of_string(string, separator):
    elements = string.strip(separator).split(separator)
    return elements


def convert_list_to_string(list_elements):
    return PATTERN_SEPARATOR.join(list_elements)
