class Empregado:
    allCargos = ['presidente', 'diretor', 'gerente', 'analista', 'auxiliar']

    def __init__(self, primeiro_nome, sobrenome, cargo, salario, taxa_reajuste):
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

    def calcular_reajuste(self, salario):
        return salario * self.taxa_reajuste

    def gerar_nome_completo(self, nome, sobrenome):
        return nome + " " + sobrenome

    def validar_cargo(self, cargo):
        if cargo in self.allCargos:
            return 'Cargo Valido'
        return 'Cargo não válido'