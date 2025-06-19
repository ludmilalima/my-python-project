def contar_bob(sequencia):
    contador = 0

    for letra in range(0, len(sequencia) - 2):
        # note that the interval being checked is [letra, letra + 3)
        if sequencia[letra:letra + 3] == "bob":
            contador += 1
    return contador

def main():
    sequencia = input("Insira uma sequência de caracteres em letras minúsculas: ")
    print("Número de ocorrências de 'bob':", contar_bob(sequencia))

if __name__ == "__main__":
    main()