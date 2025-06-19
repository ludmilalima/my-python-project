def eh_divisor(numero):
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(f"{i}\n")

def main():
    numero = int(input("Digite um número: "))
    eh_divisor(numero)

if __name__ == "__main__":
    main()