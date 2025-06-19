import numpy as np

def adivinhe_o_numero():
    numero = np.random.randint(1, 100)
    palpite = -1
    maior = 100
    menor = 1
    
    print("Adivinhe o número:\n")
    while (palpite != numero):
        palpite = int(input(f"Está entre {menor} e {maior}: "))
        if palpite < numero:
            menor = palpite
        elif palpite > numero:
            maior = palpite
        else:
            print("Parabéns! Você adivinhou o número.")

if __name__ == "__main__":
    adivinhe_o_numero()
