import numpy as np

def gerar_senha_aleatoria():
    no_de_char = np.random.randint(7, 10, size = 1)
    senha_ordinal = np.random.randint(33, 126, size = no_de_char)
    senha = ''.join([chr(i) for i in senha_ordinal])
    return senha

senha = gerar_senha_aleatoria()
print(f"A senha gerada possui {len(senha)} caracteres e é: {senha}")