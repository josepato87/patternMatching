import sys

from itertools import islice
from operator import eq

from src.utils import *

WILDCARD = '*'
PATTERN_SEPARATOR = ','
PATH_SEPARATOR = '/'
NO_MATCH_STATEMENT = 'NO MATCH'


def get_input_setup():
    inputs = (line.rstrip('\n') for line in sys.stdin)

    patterns_quantity = get_integer_from_input(inputs)
    patternsList = list(islice(inputs, patterns_quantity))

    paths_quantity = get_integer_from_input(inputs)
    paths = islice(inputs, paths_quantity)

    return patternsList, paths


def get_pattern_matches(patterns, paths):
    for path in paths:
        print(get_pattern_for_path(patterns, path))


def get_pattern_for_path(patterns, path):
    path_elements = get_elements_of_string(path, PATH_SEPARATOR)

    match_pattern = None
    match_candidates = []

    for pattern in patterns:
        pattern_elements = get_elements_of_string(pattern, PATTERN_SEPARATOR)

        if path_elements == pattern_elements:
            match_pattern = pattern_elements
            break

        is_pattern_and_path_length_equal = len(
            path_elements) == len(pattern_elements)
        pattern_has_wildcards = WILDCARD in pattern_elements

        if is_pattern_and_path_length_equal and pattern_has_wildcards:
            if is_match_candidate(pattern_elements, path_elements):
                match_candidates.append(pattern_elements)

    return get_match_pattern(match_pattern, match_candidates)


def is_match_candidate(pattern_elements, path_elements):
    pattern_wildcards_quantity = pattern_elements.count(WILDCARD)
    pattern_and_path_match_fields = map(eq, path_elements, pattern_elements)
    match_fields_quantity = sum(pattern_and_path_match_fields)

    if len(path_elements) == (pattern_wildcards_quantity + match_fields_quantity):
        return True
    else:
        return False


def get_match_pattern(match_pattern, match_candidates):
    if match_pattern:
        return convert_list_to_string(match_pattern)
    elif match_candidates:
        is_single_candidate = len(match_candidates) == 1

        if is_single_candidate:
            return convert_list_to_string(match_candidates[0])
        else:
            best_match_candidate = get_best_match_candidate(match_candidates)
            return convert_list_to_string(best_match_candidate)
    else:
        return NO_MATCH_STATEMENT


def get_best_match_candidate(match_candidates):
    fewest_wildcards = []
    wildcard_quantity = None

    for candidate in match_candidates:
        candidate_wildcards = candidate.count(WILDCARD)

        if wildcard_quantity is None:
            wildcard_quantity = candidate_wildcards
            fewest_wildcards.append(candidate)
        else:
            if candidate_wildcards < wildcard_quantity:
                wildcard_quantity = candidate_wildcards
                fewest_wildcards[:] = []
                fewest_wildcards.append(candidate)
            elif candidate_wildcards == wildcard_quantity:
                fewest_wildcards.append(candidate)

    if len(fewest_wildcards) == 1:
        return fewest_wildcards[0]
    else:
        return tie_breaker(fewest_wildcards)


def tie_breaker(pattern_elements):
    winner = None
    highest_score = None

    for pattern in pattern_elements:
        index_sum = sum([i for i, v in enumerate(pattern) if v == WILDCARD])

        if highest_score is None:
            highest_score = index_sum
            winner = pattern
        elif index_sum > highest_score:
            highest_score = index_sum
            winner = pattern

    return winner
