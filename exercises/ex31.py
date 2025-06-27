import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt

def eh_viavel(l, c):
    global c_matriz
    global l_matriz
    vertical_border = l >= 0 and l < l_matriz
    horizontal_border = c >= 0 and c < c_matriz
    return vertical_border and horizontal_border

def explorar_caminho(step, l, c):
    #top
    if(eh_viavel(l,c+1)):
        preencher_caminho(step, l, c+1)
    #bottom
    if(eh_viavel(l,c-1)):
        preencher_caminho(step, l, c-1)
    #left
    if(eh_viavel(l,c+1)):
        preencher_caminho(step, l-1, c)
    #right
    if(eh_viavel(l,c+1)):
        preencher_caminho(step, l+1, c)
    return

def preencher_caminho(step, l, c):
    global matriz
    if (matriz[l][c] == 0):
        step += 1
        matriz[l][c] = step
        explorar_caminho(step, l, c)
    return
    

def read_matrix(filename):
    global matriz
    with open(filename, 'r') as file:
        for line in file:
            # Convert each line into list of integers
            row = [int(x) for x in line.strip().split()]
            matriz.append(row)
        
        matriz_np = np.array(matriz)
        # Ensure matriz is a numpy array for pyplot rendering
        matriz.clear()
        matriz.extend(matriz_np.tolist())
    return

def busca_caminho(l,c):
    global matriz
    menor_custo = float('inf')
    menor_vizinho = []
    global menor_caminho
    if (eh_viavel(l-1,c) and matriz[l-1][c] > 0 and matriz[l-1][c] <= menor_custo):
        if(matriz[l-1][c] < menor_custo):
            menor_custo = matriz[l-1][c]
            menor_vizinho.clear()
        menor_vizinho.append([l-1, c])
    if (eh_viavel(l+1,c) and matriz[l+1][c] > 0 and matriz[l+1][c] <= menor_custo):
        if(matriz[l+1][c] < menor_custo):
            menor_custo = matriz[l+1][c]
            menor_vizinho.clear()
        menor_vizinho.append([l+1, c])
    if (eh_viavel(l,c+1) and matriz[l][c+1] > 0 and matriz[l][c+1] <= menor_custo):
        if(matriz[l][c+1] < menor_custo):
            menor_custo = matriz[l][c+1]
            menor_vizinho.clear()
        menor_vizinho.append([l, c+1])
    if (eh_viavel(l,c-1) and matriz[l][c-1] > 0 and matriz[l][c-1] <= menor_custo):
        if(matriz[l][c-1] < menor_custo):
            menor_custo = matriz[l][c-1]
            menor_vizinho.clear()
        menor_vizinho.append([l, c-1])

    for item in menor_vizinho:
        l = item[0]
        c = item[1]
        matriz[l][c] = -2
        menor_caminho.append(item)
    return

def possiveis_caminhos():
    global menor_caminho
    global l_queijo
    global c_queijo
    while (len(menor_caminho) > 0):
        item = menor_caminho.pop(0)
        l = item[0]
        c = item[1]
        busca_caminho(l, c)
        if (l == l_queijo and c == c_queijo):
            menor_caminho.clear()
    return

def get_random_coordinates():
    global l_matriz
    global c_matriz
    l = np.random.randint(0, l_matriz)
    c = np.random.randint(0, c_matriz)
    while (matriz[l][c] == -1):
        l = np.random.randint(0, l_matriz)
        c = np.random.randint(0, c_matriz)
    return l, c

matriz = []
read_matrix('/workspaces/my-python-project/exercises/files/labirinto-grande.txt')
matriz_shape = np.shape(matriz)
l_matriz = matriz_shape[0]
c_matriz = matriz_shape[1]
l_rato, c_rato = get_random_coordinates()
l_queijo , c_queijo = get_random_coordinates()
menor_caminho = [(l_rato, c_rato)]
preencher_caminho(0, l_queijo, c_queijo)
possiveis_caminhos()

cmap = colors.ListedColormap(['red', 'black', 'white'])
bounds = [-2.5, -1.5, -0.5, 1000]
norm = colors.BoundaryNorm(bounds, cmap.N)

plt.text(c_queijo, l_queijo, 'Q', color='yellow', fontsize=12, ha='center', va='center', fontweight='bold', zorder=11)
plt.text(c_rato, l_rato, 'R', color='gray', fontsize=12, ha='center', va='center', fontweight='bold', zorder=11)

plt.imshow(matriz, cmap=cmap, norm=norm)
plt.savefig('caminho.png')
plt.show()