import unittest
from empregado_sample import Empregado

print (Empregado('Caique', 'Antunes', 'Tomadora de Cafe', 'Junior', 2000))


class Teste_Empregado(unittest.TestCase):
    def test_calcular_reajuste(self):
        self.assertEqual(Empregado.calcular_reajuste(Empregado.retornasalario, Empregado.retornataxa_reajuste),2100)

    def test_fullname(self):
        self.assertEqual(Empregado.calcular_reajuste(Empregado.retornaPnome, Empregado.retornasobrenome),'Caique Antunes')

    def test_fullname(self):
        self.assertEqual(Empregado.calcular_reajuste(Empregado.retornacargo),'Cargo Valido')


# * calcular_reajuste, o qual irá exibir o novo salario do funcionario, baseado no salário atual e sua taxa de reajuste;
# * gerar_nome_completo, que combinara seus ambos os nomes e exibir o nome completo do funcionário;
# * validar_cargo, que deverá verificar se o cargo atual está dentro de uma lista de cargos implementados pela empresa (presidente, diretor, gerente, analista e auxiliar)