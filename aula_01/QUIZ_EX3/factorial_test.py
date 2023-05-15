import unittest
from factorial_sample import Factorial_Sample

class Test_Factorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(Factorial_Sample.factorial(5),120)
        self.assertEqual(Factorial_Sample.factorial(0), 1)
        self.assertEqual(Factorial_Sample.factorial(1), 1)
        self.assertEqual(Factorial_Sample.factorial(2), 2)
        self.assertEqual(Factorial_Sample.factorial(10), 3628800)
        self.assertEqual(Factorial_Sample.factorial(6), 720)
        self.assertEqual(Factorial_Sample.factorial(3), 6)
