def meeus_jones_butcher(x): #válido para x > 1583
    resto_a = x % 19
    quociente_b = x // 100
    resto_c = x % 100
    quociente_d = quociente_b // 4
    resto_e = quociente_b % 4
    quociente_f = (quociente_b + 8) // 25
    quociente_g = (quociente_b - quociente_f + 1) // 3
    resto_h = ((19 * resto_a) + quociente_b - quociente_d - quociente_g + 15) % 30
    quociente_i = resto_c // 4
    resto_k = resto_c % 4
    resto_l = (32 + (2 * resto_e) + (2 * quociente_i) - resto_h - resto_k) % 7
    quociente_m = (resto_a + (11 * resto_h) + (22 * resto_l)) // 451
    quociente_n = (resto_h + resto_l - (7 * quociente_m) + 114) // 31
    resto_p =  (resto_h + resto_l - (7 * quociente_m) + 114) % 31

    print(f"A páscoa será em {resto_p + 1} do mês {quociente_n} no ano {x}.")

meeus_jones_butcher(int(input("Insira o ano de interesse:")))