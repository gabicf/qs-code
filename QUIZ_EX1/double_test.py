import unittest
from double_sample import DoubleSample

class DoubleTest(unittest.TestCase):
    def testDoble1 (self):
        self.assertEqual(DoubleSample.double(5),25)

    def testDoble2 (self):
        self.assertEqual(DoubleSample.double(-3),9)

    def testDoble3 (self):
        self.assertEqual(DoubleSample.double(0),0)

    
