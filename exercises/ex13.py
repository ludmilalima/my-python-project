def decimal_para_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return binario

def main():
    numero = int(input("Digite um número decimal: "))
    binario = decimal_para_binario(numero)
    print(f"O número {numero} em binário é: {binario}")

if __name__ == "__main__":
    main()