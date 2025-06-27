import numpy as np
import matplotlib.pyplot as plt

def ajuste_linear():
    lista_de_pontos = np.genfromtxt('./exercises/files/dados-linear2.csv', delimiter=',', skip_header=1)
    x_values = lista_de_pontos[:,0]
    y_values = lista_de_pontos[:,1]

    sum_x = sum(x_values)
    sum_x2 = sum(x * x for x in x_values)
    sum_y = sum(y_values)
    sum_xy = sum(x_values[i] * y_values[i] for i in range(len(x_values)))
    x_avg = sum_x / len(x_values)
    y_avg = sum_y / len(y_values)

    m = ((len(x_values) * sum_xy) - (sum_x * sum_y)) / ((len(x_values) * sum_x2) - (sum_x * sum_x))
    b = y_avg - (m * x_avg)

    plt.scatter(x_values, y_values, color='blue', label='Data Points')
    
    # Plot the linear fit line
    fit_line = m * x_values + b
    plt.plot(x_values, fit_line, color='red', label='Linear Fit')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression Fit')
    plt.legend()
    plt.grid(True)
    plt.show()
    # Save plot to file before showing it
    plt.savefig('linear_regression.png')
    print(f"{m:.2f}x + ({b:.2f})")

ajuste_linear()