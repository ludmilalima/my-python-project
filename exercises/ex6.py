def max_divisor_comum(m, n):
    mdc = min(m, n)
    while mdc > 0:
        if m % mdc == 0 and n % mdc == 0:
            return mdc
        mdc -= 1

def main():
    m = int(input("Digite o primeiro número: "))
    n = int(input("Digite o segundo número: "))
    resultado = max_divisor_comum(m, n)
    print(f"O máximo divisor comum de {m} e {n} é {resultado}")

if __name__ == "__main__":
    main()