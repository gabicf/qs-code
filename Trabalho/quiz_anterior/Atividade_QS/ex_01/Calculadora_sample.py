class Calculadora_Sample:

    @staticmethod
    def somar(n1, n2):
        return n1 + n2
    

    def subtrair(n1, n2):
        return n1 - n2
    

    def multiplicar(n1, n2):
        return n1*n2
    

    def dividir(n1, n2):
        if n2 == 0:
            return "NÃO É POSSIVEL DIVIDIR POR ZERO"
        return n1 /n2
    