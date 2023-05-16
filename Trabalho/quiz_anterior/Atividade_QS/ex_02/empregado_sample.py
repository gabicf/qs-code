class Empregado:
    def __init__(self, primeiro_nome, sobrenome, cargo, salario, taxa_reajuste = 1.05):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.cargo = cargo
        self.salario = salario
        self.taxa_reajuste = taxa_reajuste

    def retornaPnome(self):
        return self.primeiro_nome
    
    def retornasobrenome(self):
        return self.sobrenome

    def retornacargo(self):
        return self.cargo

    def retornasalario(self):
        return self.salario

    def retornataxa_reajuste(self):
        return self.taxa_reajuste

    @staticmethod
    def calcular_reajuste():
        pass

    def gerar_nome_completo():
        pass

    def validar_cargo():
        pass


# * calcular_reajuste, o qual irá exibir o novo salario do funcionario, baseado no salário atual e sua taxa de reajuste;
# * gerar_nome_completo, que combinara seus ambos os nomes e exibir o nome completo do funcionário;
# * validar_cargo, que deverá verificar se o cargo atual está dentro de uma lista de cargos implementados pela empresa (presidente, diretor, gerente, analista e auxiliar)