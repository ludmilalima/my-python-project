def nao_eh_triangulo(a, b, c):

    # check python operators precedence https://runestone.academy/ns/books/published/fopp/Conditionals/PrecedenceofOperators.html
    a_nao_eh_maior = a < (b + c)
    b_nao_eh_maior = b < (a + c)
    c_nao_eh_maior = c < (a + b)

    return (a_nao_eh_maior and b_nao_eh_maior and c_nao_eh_maior)

def main():
    a = int(input("Digite o valor do lado A: "))
    b = int(input("Digite o valor do lado B: "))
    c = int(input("Digite o valor do lado C: "))

    if nao_eh_triangulo(a, b, c):
        print("Os valores não formam um triângulo.")
    else:
        print("Os valores formam um triângulo.")

if __name__ == "__main__":
    main()