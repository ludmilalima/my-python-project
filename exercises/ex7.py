def numero_de_vogais(sequencia):
    vogais = "aeiou"
    contador = 0
    for letra in sequencia:
        if letra in vogais:
            contador += 1
    return contador

def main():
    sequencia = input("Insira uma sequência composta unicamente por letras minúsculas:")
    print("Número de vogais:", numero_de_vogais(sequencia))

if __name__ == "__main__":
    main()