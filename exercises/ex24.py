def fibonacci_recursivo(n):
    print(f"----- início da função, recebeu {n} como argumento")
    if n == 0:
        print(f"a(0) = 0")
        return 0
    elif n == 1:
        print(f"a(1)= 1")
        return 1
    else:
        print(f"chamada recursiva para n = {n-1}")
        an_1 = fibonacci_recursivo(n-1)
        print(f"retorno da chamada recursiva para n = {n-1}")
        print(f"chamada recursiva para n = {n-2}")
        an_2 = fibonacci_recursivo(n-2)
        print(f"retorno da chamada recursiva para n = {n-2}")
        an = an_1 + an_2
        print(f"a({n}) = a({n-1}) + a({n-2}) = {an_1} + {an_2} = {an}")
        return  an
    
fibonacci_recursivo(5)

"""
a(5) = a(4) + a(3)
a(4) = a(3)' + a(2)
a(3) = a(2)' + a(1)
a(2) = a(1)' + a(0)
a(1) = 1
a(0) = 0

a(5) = a(1) + a(0) + a(1) + a(1) + a(0) + a(1) + a(0) + a(1)
a(5) = 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 = 5
"""