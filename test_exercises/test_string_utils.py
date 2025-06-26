import pytest
import exercises.string_utils as su


@pytest.mark.parametrize('word, expected_reversal', [('hello', 'olleh'), (' ', ' '), ('madam', 'madam')])
def test_reverse_text(word, expected_reversal):
    assert su.reverse_text(word) == expected_reversal