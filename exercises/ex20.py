from decimal import Decimal
def aproximar_raiz_com_Decimal(x):
    raiz = Decimal(x/2)
    raiz_antiga = Decimal(0)
    n_com_decimal = 0

    while abs(Decimal(raiz * raiz - x)) >= Decimal(1e-12) or raiz_antiga == raiz:
        raiz_antiga = raiz
        raiz = Decimal((raiz + (Decimal(x/raiz)))/2)
        n_com_decimal += 1
        print(f"Raiz atual: {raiz:.50f}")
        print(f"Iteração {n_com_decimal}: {abs(Decimal(raiz * raiz - x)):.15f} >= {Decimal(1e-12):.15f}\n")
    return raiz

def aproximar_raiz_sem_Decimal(x):
    raiz = x / 2
    raiz_antiga = 0
    n_sem_decimal = 0

    while abs(raiz * raiz - x) >= 1e-12 and raiz_antiga != raiz:
        raiz_antiga = raiz
        raiz = (raiz + (x/raiz)) / 2
        n_sem_decimal += 1
        print(f"Raiz atual: {raiz:.50f}")
        print(f"Iteração {n_sem_decimal}: {abs(Decimal(raiz * raiz - x)):.15f} >= {Decimal(1e-12):.15f}\n")

    return raiz

x = int(input("Digite um número: "))
raiz_com_decimal = Decimal(aproximar_raiz_com_Decimal(x))
raiz_sem_decimal = aproximar_raiz_sem_Decimal(x)
print(f"A raiz quadrada aproximada de {x} COM Decimal\n{raiz_com_decimal:.50f}\n{raiz_com_decimal*raiz_com_decimal:.50f}")
print(f"A raiz quadrada aproximada de {x} SEM Decimal\n{raiz_sem_decimal:.50f}\n{raiz_sem_decimal*raiz_sem_decimal:.50f}")
