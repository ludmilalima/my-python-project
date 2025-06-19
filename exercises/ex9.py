def maior_sequencia_alfabetica(sequencia):
    inicio_atual = 0
    inicio_maior = 0
    maior = 0
    atual = 1

    for i in range(1, len(sequencia)):
        # check for Unicode (ASCII) table https://en.wikipedia.org/wiki/List_of_Unicode_characters
        if sequencia[i] >= sequencia[i - 1]:
            atual += 1
        else:
            atual = 1
            inicio_atual = i

        if atual > maior:
            maior = atual
            inicio_maior = inicio_atual

    return sequencia[inicio_maior:inicio_maior + maior]

def main():
    sequencia = input("Digite uma sequência de caracteres: ")
    resultado = maior_sequencia_alfabetica(sequencia)
    print(f"A maior sequência alfabética é: {resultado}")

if __name__ == "__main__":
    main()