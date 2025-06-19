def converter():
    romanos = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    def converter_em_romano(numero):
        resultado = ''
        temp = numero

        for simbolo, valor in reversed(romanos.items()):
            while temp >= valor:
                resultado += simbolo
                temp -= valor
        return resultado
    
    def converter_em_inteiro(romano):
        total = 0
        i = 0

        while i < len(romano):
            if (i + 1 < len(romano) and 
                romano[i:i+2] in romanos):
                total += romanos[romano[i:i+2]]
                i += 2
            else:
                total += romanos[romano[i]]
                i += 1
        return total
        
    convertidos_em_romano = {num: converter_em_romano(num) for num in range(1, 4000)}
    convertidos_em_inteiro = {romano: converter_em_inteiro(romano) for romano in convertidos_em_romano.values()}

    print("Conversão de números romanos para inteiros:")
    for numero, romano in convertidos_em_romano.items():
        print(f"{numero} -> {romano}")

    print("Conversão de números romanos para inteiros:")
    for romano, numero in convertidos_em_inteiro.items():
        print(f"{romano} -> {numero}")


if __name__ == "__main__":
    converter()
