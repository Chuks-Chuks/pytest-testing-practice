import pytest
import functions.shapes as shapes

class TestRectangle:

    def test_area(self, my_rectangle):
        assert shapes.Rectangle(10, 20).area() == my_rectangle.length * my_rectangle.width

    @pytest.mark.maths
    def test_not_equal(self, my_rectangle, weird_rectangle):
        assert my_rectangle != weird_rectangle