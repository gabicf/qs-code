import unittest
from power_sample import PowerSample

class PowerTest(unittest.TestCase):
    def powerTest1 (self):
        """Testando a primeira equação de 2 e 3 """
        self.assertEqual(PowerSample.power(2,3),8)

    def powerTest2(self):
        """Testando a primeira equação de 2 e 3 """
        self.assertEqual(PowerSample.power(10,2),100)

    def powerTest3(self):
        """Testando a primeira equação de 2 e 3 """
        self.assertEqual(PowerSample.power(3,4),81)

    def powerTest4(self):
        """Testando a primeira equação de 2 e 3 """
        self.assertEqual(PowerSample.power(5,0),1)

    def powerTest5(self):
        """Testando a primeira equação de 2 e 3 """
        self.assertEqual(PowerSample.power(2,-1),0.5)
    