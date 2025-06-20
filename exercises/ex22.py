import numpy as np

def gerar_senha_forte():
    no_caracteres = 0
    senha_ordinal = []
    valida = False
    no_tentativas = 0

    while not valida:
        no_tentativas += 1
        no_caracteres = np.random.randint(7, 10, size = 1)
        senha_ordinal = np.random.randint(33, 126, size = no_caracteres)
        senha = ''.join([chr(i) for i in senha_ordinal])
        
        if (any(c.islower() for c in senha) and
            any(c.isupper() for c in senha) and
            any(c.isdigit() for c in senha) and
            len(senha_ordinal) >= 8 ):
            valida = True
        
        print(f"Tentativa {no_tentativas}: {senha} contem {len(senha_ordinal)} caracteres.")

    return senha

senha = gerar_senha_forte()
print(f"A senha gerada possui {len(senha)} caracteres e é: {senha}")