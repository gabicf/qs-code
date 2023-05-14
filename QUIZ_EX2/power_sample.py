class PowerSample:

    @staticmethod
    def power(base, exponent):
        if exponent == 0:
            return 1
        if exponent < 0:
            return 1 / PowerSample.power(base, -exponent)
        else:
            return base * PowerSample.power(base, exponent - 1)