import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturedemo1(self):
        print("First Demo")

    def test_fixturedemo2(self):
        print("Second Demo")

    def test_fixturedemo3(self):
        print("Third Demo")

    def test_fixturedemo4(self):
        print("Forth Demo")

