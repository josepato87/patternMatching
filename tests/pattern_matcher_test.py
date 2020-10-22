from io import StringIO

import pytest

from src.pattern_matcher import get_input_setup, is_match_candidate


def test_get_input_setup(monkeypatch):
    string_input = StringIO(
        '2\n'
        'pattern-1\n'
        'pattern-2\n'
        '2\n'
        'path-1\n'
        'path-2\n'
    )
    monkeypatch.setattr('sys.stdin', string_input)
    expected_patterns = ['pattern-1', 'pattern-2']
    expected_paths = ['path-1', 'path-2']

    patternsList, paths = get_input_setup()

    assert all([a == b for a, b in zip(patternsList, expected_patterns)])
    assert all([a == b for a, b in zip(paths, expected_paths)])


@pytest.mark.parametrize('pattern, path, expected_result', [
    (['a', '*', 'c'], ['a', 'b', 'c'], True),
    (['a', '*', 'c'], ['x', 'y', 'z'], False)
])
def test_is_match_candidate(pattern, path, expected_result):
    assert is_match_candidate(pattern, path) == expected_result




