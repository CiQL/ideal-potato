import unittest
from fac import factorial as fac

class Factorial(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(fac(-1), 1)
    def test_zero(self):
        self.assertEqual(fac(0), 1)
    def test_positive(self):
        self.assertEqual(fac(5), 120)

if __name__ == "__main__":
    unittest.main()
