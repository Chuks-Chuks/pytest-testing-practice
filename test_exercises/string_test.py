import pytest
import exercises.strings_exercises as se

class TestStrings:

    def test_uppercase(self):
        assert se.uppercase(word='hello') == 'HELLO'

    def test_split(self):
        assert isinstance(se.split(word='The boy is coming'), list)

    def test_wrong_case(self):
        assert se.uppercase(word='test') == 'Test'