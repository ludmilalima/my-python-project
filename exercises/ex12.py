def binario_para_decimal(base_binaria):
    digitos_restantes = len(base_binaria) - 1
    base_decimal = 0
    base_binaria_invertida = base_binaria[::-1]

    while digitos_restantes >= 0:
        digito = int(base_binaria_invertida[digitos_restantes])
        base_decimal += digito * (2 ** (digitos_restantes))
        digitos_restantes -= 1

    return base_decimal

def main():
    base_binaria = input("Insira um número binário: ")
    base_decimal = binario_para_decimal(base_binaria)
    print(f"O número {base_binaria} em decimal é: {base_decimal}")

if __name__ == "__main__":
    main()