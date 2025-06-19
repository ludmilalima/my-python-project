def apenas_pares(lista):
    lista_de_pares = [number for number in lista if number % 2 == 0]
    return lista_de_pares

def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = apenas_pares(numeros)
    print("Números pares:", pares)

if __name__ == "__main__":
    main()