import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def teardown(self):
        print("\nВыполнение метода Teardown")

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(6, 2) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(5, 3) == 2

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(1, 1) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)