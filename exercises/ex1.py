def eh_bissexto(year):
    divisivel_por_400 = year % 400 == 0
    divisivel_por_100 = year % 100 == 0
    divisivel_por_4 = year % 4 == 0
    return (divisivel_por_400 or (divisivel_por_4 and not divisivel_por_100))

def main():
    ano_texto = input("Digite um ano: ")
    ano = int(ano_texto)
    if eh_bissexto(ano):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")
        
if __name__ == "__main__":
    main()