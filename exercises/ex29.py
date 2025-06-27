import numpy as np
import matplotlib.pyplot as plt

def triangulo_de_pascal(n):
    matriz_nxn = np.zeros((n,n))
    for i in range(0, n):
        for j in range(0, i+1):
            if (j == 0 or j == i):
                matriz_nxn[i,j] = 1
            elif (j > 0 and j < i):
                matriz_nxn[i,j] = (matriz_nxn[i-1,j] + matriz_nxn[i-1, j-1]) % 2
        print(f"{matriz_nxn[i, 0:i+1]}")
    return matriz_nxn

triangulo = triangulo_de_pascal(int(input("Insira a altura do triângulo:")))
plt.imshow(triangulo)
plt.savefig('triangulo.png')
plt.show()
