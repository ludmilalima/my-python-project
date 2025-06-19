from decimal import Decimal


def pi_como_serie_decimal():
    start = Decimal('2.0')
    pi = Decimal('0.0')
    numerador = Decimal('-1.0')
    denominador = Decimal('1.0')

    for i in range(1, 16):
        numerador *= Decimal('-1.0')
        denominador  = Decimal(start * (start + Decimal('1.0')) * (start + Decimal('2.0')))
        pi += numerador / denominador
        start += Decimal('2.0')
        print(f"Iteração {i}: {pi}")

    return pi

def pi_como_serie():
    start = 2.0
    pi = 0.0
    numerador = -1.0
    denominador = 1.0

    for i in range(1, 16):
        numerador *= -1.0
        denominador  = start * (start + 1.0) * (start + 2.0)
        pi += numerador / denominador
        start += 2.0
        print(f"Iteração {i}: {pi}")

    return pi

def main():
    pi = pi_como_serie()
    pi_decimal = pi_como_serie_decimal()

    print(f"Valor de pi: {pi:.15f}")
    print(f"Valor de pi com Decimal: {pi_decimal:.15f}")
    print(f"Valor de pi: {pi:.50f}")
    print(f"Valor de pi com Decimal: {pi_decimal:.50f}")

if __name__ == "__main__":
    main()