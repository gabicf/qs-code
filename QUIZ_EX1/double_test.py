import unittest
from double_sample import DoubleSample

class DoubleTest(unittest.TestCase):
    def testDoble1 (self):
        """Testa se o número 5 elevado ao quadrado é igual a 25 """
        self.assertEqual(DoubleSample.double(5),25)

    def testDoble2 (self):
        """Testa se o número -3 elevado ao quadrado é igual a 9. """
        self.assertEqual(DoubleSample.double(-3),9)

    def testDoble3 (self):
        """Testa se o número 0 elevado ao quadrado é igual a 0 """
        self.assertEqual(DoubleSample.double(0),0)


    
