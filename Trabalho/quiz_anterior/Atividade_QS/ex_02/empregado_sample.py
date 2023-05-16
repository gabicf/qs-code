import unittest
from empregado_sample import Empregado

class Teste_Empregado(unittest.TestCase):
    def test_calcular_reajuste(self):
        empregado = Empregado('Caique', 'Antunes', 'Programador', 2000, 1.05)
        self.assertEqual(empregado.calcular_reajuste(empregado.retornasalario()), 2100)

    def test_fullname(self):
        empregado = Empregado('Caique', 'Antunes', 'Programador', 2000, 1.05)
        self.assertEqual(empregado.gerar_nome_completo(empregado.retornaPnome(), empregado.retornasobrenome()), 'Caique Antunes')

    def test_valida_cargo(self):
        empregado = Empregado('Caique', 'Antunes', 'Programador', 2000, 1.05)
        self.assertEqual(empregado.validar_cargo(empregado.retornacargo()), 'Cargo Valido')
