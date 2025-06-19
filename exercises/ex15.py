from decimal import Decimal


def cosseno_como_serie(x):
    criterio_de_encerramento = Decimal('1e-6') 
    termo = Decimal('1.0')
    acumulado = Decimal('1.0')
    numerador = Decimal('1.0')
    denominador = Decimal('1.0')
    n = 2

    while abs(termo) > criterio_de_encerramento:
        numerador *= Decimal(-x * x)
        denominador *= Decimal(n * (n - 1))
        termo = numerador / denominador
        acumulado += termo
        n += 2

    return acumulado

def main():
    x = float(input("Digite o valor de x: "))
    resultado = cosseno_como_serie(x)
    print(f"O cosseno de {x} calculado como série é: {resultado}")

if __name__ == "__main__":
    main()