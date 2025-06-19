def tempo_em_segundos(segundos):
    dias = (segundos) // (3600*24) #floor
    horas = (segundos % (3600*24)) // 3600 # floor
    minutos = (segundos % 3600) // 60 # mod + floor
    segundos_restantes = segundos % 60 # mod

    return dias, horas, minutos, segundos_restantes

def main():
    segundos = int(input("Digite o tempo em segundos: "))
    dias, horas, minutos, segundos_restantes = tempo_em_segundos(segundos)
    print(f"{dias} dia(s), {horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s)")

if __name__ == "__main__":
    main()