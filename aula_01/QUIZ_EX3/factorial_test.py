import unittest
from factorial_sample import Factorial_Sample

class Test_Factorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(Factorial_Sample.factorial(5),120)

