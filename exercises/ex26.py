import numpy as np

def max_da_lista(n):
    lista_aleatoria = np.random.randint(1,100, size = n)
    maior_valor = 0

    for index in range(0, n):
        maior_valor = max(maior_valor, lista_aleatoria[index])
        print(f"i = {n}, lista_aleatoria[{n}] = {lista_aleatoria[index]}")

    return maior_valor

n = int(input("Insira o comprimento da lista:"))
maior_valor = max_da_lista(n)
print(f"Maior valor: {maior_valor}")