import pytest
import time
import functions.my_functions as myf

def test_add():
    result = myf.add(1, 4)
    assert result == 5

def test_divide():
    result = myf.divide(10, 5)
    assert result == 2

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = myf.divide(10, 5)
    assert result == 2

@pytest.mark.skip(reason='This feature is currently broken')
def test_skip():
    assert myf.divide(10, 5) == 2