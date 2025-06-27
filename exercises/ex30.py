import numpy as np

def coordenadas_proximo_movimento(l, c, n):
    new_l = (l-1) % n
    if (new_l < 0):
        new_l = n - 1
    new_c = (c+1) % n

    return new_l, new_c

def gerar_quadrado_magico(n):
    quadrado = np.zeros((n,n))
    new_linha = -1
    new_coluna = -1
    linha = 0
    coluna = n // 2 # não precisa somar 1 pq começa em 0
    elementos_preenchidos = 0

    while (elementos_preenchidos < n * n):
        elementos_preenchidos += 1
        quadrado[linha, coluna] = elementos_preenchidos
        new_linha, new_coluna = coordenadas_proximo_movimento(linha, coluna, n)

        if(quadrado[new_linha, new_coluna] == 0):
            linha = new_linha
            coluna = new_coluna
        else:
            while(quadrado[linha, coluna] != 0 and elementos_preenchidos < n * n):
                linha = (linha + 1) % n
    return quadrado

n = int(input("Insira o valor de n:"))
quadrado_magico = gerar_quadrado_magico(n)
for i in range(0, n):
    print(f"{quadrado_magico[i, 0:n]}")

