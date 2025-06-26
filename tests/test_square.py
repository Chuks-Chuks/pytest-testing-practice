import pytest
import functions.shapes as shapes


@pytest.mark.parametrize("length, width, expected_area", [(5, 5, 25), (4, 4, 16), (7, 7, 49)])
def test_multiple_square_areas(length, width, expected_area):
    assert shapes.Square(length=length, width=width).area() == expected_area
