def fatorial_recursivo(n):
    
    if n == 0 or n == 1:
        print(f"n: {n}, resultado: 1")
        return 1
    else:
        print(f"chamada recursiva com n: {n}")
        resultado_parcial = n * fatorial_recursivo(n - 1)
        print(f"retorno da chamada recursiva com n: {n}")
        print(f"n: {n}, resultado: {resultado_parcial}")
        return resultado_parcial

def fatorial_iterativo(n):
    resultado = 1
    print(f"n: 1, resultado: {resultado}")
    for i in range(2, n + 1):
        resultado *= i
        print(f"n: {i}, resultado: {resultado}")
    return resultado

print("\n ------------- Fatorial Recursivo:")
fatorial_recursivo(5)
print("\n ------------- Fatorial Iterativo:")
fatorial_iterativo(5)