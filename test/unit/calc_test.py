import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
#Se agregan las siguientes pruebas unitarias

    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(2, 0))
        self.assertEqual(0, self.calc.power(0, 2))

    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.sqrt(4))
        self.assertAlmostEqual(1.41421356, self.calc.sqrt(2), places=8)

    def test_sqrt_method_fails_with_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, -2)

    def test_log10_method_returns_correct_result(self):
        self.assertAlmostEqual(1, self.calc.log10(10), places=8)
        self.assertAlmostEqual(2, self.calc.log10(100), places=8)

    def test_log10_method_fails_with_non_positive_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -10)
        #prueba de casos de error
        
    def test_divide_by_zero():
        with pytest.raises(ZeroDivisionError):
            Calculator.divide(5, 0)

    def test_sqrt_negative_number():
        with pytest.raises(ValueError):
            Calculator.sqrt(-5)

    def test_log10_zero_or_negative():
        with pytest.raises(ValueError):
            Calculator.log10(0)
        with pytest.raises(ValueError):
            Calculator.log10(-5)
