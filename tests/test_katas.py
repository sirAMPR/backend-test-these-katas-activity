import unittest
from katas import add, multiply, power, factorial, fibonacci


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(9), 21)


if __name__ == '__main__':
    unittest.main()
