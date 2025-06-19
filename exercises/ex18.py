from ex1 import eh_bissexto

def dia_seguinte(data):
    ultimo_dia_mes = {
        1: 31,  # Janeiro
        2: 28,  # Fevereiro
        3: 31,  # Março
        4: 30,  # Abril
        5: 31,  # Maio
        6: 30,  # Junho
        7: 31,  # Julho
        8: 31,  # Agosto
        9: 30,  # Setembro
        10: 31,  # Outubro
        11: 30,  # Novembro
        12: 31   # Dezembro
    }

    def ano_bissexto(ano):
        return eh_bissexto(ano)
    
    if data[0] == ultimo_dia_mes[data[1]]:
        if data[1] == 2 and ano_bissexto(data[2]):
            return (29, 2, data[2])
        elif data[1] < 12:
            return (1, data[1] + 1, data[2])
        else:
            return (1, 1, data[2] + 1)
    return (data[0] + 1, data[1], data[2])

def main():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    data = (dia, mes, ano)
    print("Data seguinte:", dia_seguinte(data))

if __name__ == "__main__":
    main()
