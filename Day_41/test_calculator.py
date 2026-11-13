
import unittest

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    is_even,
    calculate_grade
)


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_even_number(self):
        self.assertTrue(is_even(10))

    def test_odd_number(self):
        self.assertFalse(is_even(7))

    def test_grade_A(self):
        self.assertEqual(calculate_grade(90), "A")

    def test_grade_B(self):
        self.assertEqual(calculate_grade(70), "B")

    def test_grade_C(self):
        self.assertEqual(calculate_grade(50), "C")

    def test_grade_F(self):
        self.assertEqual(calculate_grade(30), "F")

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            calculate_grade(110)


if __name__ == "__main__":
    unittest.main()
