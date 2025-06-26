import pytest
import exercises.calculator as cal

@pytest.fixture
def numbers():
    return {
        'a': 10,
        'b': 5
    }

def test_divide(numbers):
    assert cal.divide(numbers['a'], numbers['b']) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        cal.divide(10, 0)