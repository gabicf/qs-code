import unittest
from Calculadora_sample import Calculadora_Sample


class Calculadora_Test(unittest.TestCase):

    def test_soma1(self):
        self.assertEqual(Calculadora_Sample.somar(1,1),2)

    def test_soma2(self):
        self.assertEqual(Calculadora_Sample.somar(4,5),9)

    # def test_soma3(self):
    #     self.assertEqual(Calculadora_Sample.somar(10,10),20)



        
    def test_sub1(self):
        self.assertEqual(Calculadora_Sample.subtrair(1,1),0)

    # def test_sub2(self):
    #     self.assertEqual(Calculadora_Sample.subtrair(4,2),2)

    # def test_sub3(self):
    #     self.assertEqual(Calculadora_Sample.subtrair(15,3),12)


        

    def test_mult1(self):
        self.assertEqual(Calculadora_Sample.multiplicar(1,1),1)

    # def test_mult2(self):
    #     self.assertEqual(Calculadora_Sample.multiplicar(4,4),16)

    # def test_mult3(self):
    #     self.assertEqual(Calculadora_Sample.multiplicar(10,10),100)
        




    def test_div1(self):
        self.assertEqual(Calculadora_Sample.dividir(1,1),1)

    # def test_div2(self):
    #     self.assertEqual(Calculadora_Sample.dividir(1,0),0)

    # def test_div3(self):
    #     self.assertEqual(Calculadora_Sample.dividir(10,5),2)
        