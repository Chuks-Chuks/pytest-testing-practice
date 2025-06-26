import pytest
import functions.shapes as shapes

@pytest.fixture(scope="session")
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture(scope="session")
def weird_rectangle():
    return shapes.Rectangle(5, 6)
