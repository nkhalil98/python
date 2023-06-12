import calc
import unittest


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 5), 7)
        self.assertEqual(calc.add(-2, -5), -7)
        self.assertEqual(calc.add(-2, 5), 3)
        self.assertEqual(calc.add(2, -5), -3)
        self.assertEqual(calc.add(0, 5), 5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(2, 5), -3)
        self.assertEqual(calc.subtract(-2, -5), 3)
        self.assertEqual(calc.subtract(-2, 5), -7)
        self.assertEqual(calc.subtract(2, -5), 7)
        self.assertEqual(calc.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 5), 10)
        self.assertEqual(calc.multiply(-2, -5), 10)
        self.assertEqual(calc.multiply(-2, 5), -10)
        self.assertEqual(calc.multiply(2, -5), -10)
        self.assertEqual(calc.multiply(0, 5), 0)
        self.assertEqual(calc.multiply(1, 5), 5)

    def test_divide(self):
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertEqual(calc.divide(5, -2), -2.5)
        self.assertEqual(calc.divide(-5, 2), -2.5)
        self.assertEqual(calc.divide(-5, -2), 2.5)
        self.assertEqual(calc.divide(0, 5), 0)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(5, 0)


unittest.main()
