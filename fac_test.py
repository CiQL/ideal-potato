import unittest
from fac import factorial as fac

class Factorial(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(fac(-1), 1)
    def test_zero(self):
        self.assertEqual(fac(0), 1)
    def test_positive(self):
        self.assertEqual(fac(5), 120)
    def test_hundred(self):
        self.assertEqual(fac(100), 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)


if __name__ == "__main__":
    unittest.main()
