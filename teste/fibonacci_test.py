import unittest
from math_samples import MathSamples

class FibonacciTest(unittest.TestCase):

    def teste_fib02(self):
        """Testando casopara entrada = 1"""
        self.assertEqual(
            MathSamples.fibonacci(1),
            1
            
        )