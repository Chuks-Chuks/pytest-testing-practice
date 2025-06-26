import pytest
import exercises.test_maths_ops as tmo

@pytest.mark.maths
class TestMathematics:

    @pytest.mark.parametrize('x, y, expected_value', [(10, 5, 15), (1, 3, 4), (-1, -3, -4)])
    def test_add(self, x, y, expected_value):
        add_class = tmo.Mathematics(x, y)
        assert add_class.add() == expected_value