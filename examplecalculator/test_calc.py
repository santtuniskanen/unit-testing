import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(5, 6), 11)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(1, 2), -1)
        self.assertEqual(calc.subtract(5, 6), -1)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(1, 2), 2)
        self.assertEqual(calc.multiply(5, 6), 30)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(1, 2), 0.5)
        self.assertEqual(calc.divide(5, 1), 5)
        self.assertEqual(calc.divide(-1, -1), 1)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()