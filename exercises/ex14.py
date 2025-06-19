def conversao_rgb(cor_em_hexadecimal):
    hexadecimal = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    
    def rgb_hexadecimal_para_decimal(cor_hex):
        # remover '#' se presente e garantir que a string esteja em maiúsculas
        cor_hex = cor_hex.lstrip('#').upper()

        r_hex = cor_hex[0:2]
        g_hex = cor_hex[2:4]
        b_hex = cor_hex[4:6]

        r = hexadecimal[r_hex[0]] * 16 + hexadecimal[r_hex[1]]
        g = hexadecimal[g_hex[0]] * 16 + hexadecimal[g_hex[1]]
        b = hexadecimal[b_hex[0]] * 16 + hexadecimal[b_hex[1]]

        # r = int(cor_hex[0:2], 16)
        # g = int(cor_hex[2:4], 16)
        # b = int(cor_hex[4:6], 16)

        return (r, g, b)
    
    def decimal_para_hexadecimal(numero):
        hex = ''
        if numero == 0:
            return '00'
        while numero > 0:
            resto = numero % 16
            hex = str([indice for indice, valor in hexadecimal.items() if valor == resto][0]) + hex
            numero //= 16
        return hex

    def rgb_decimal_para_hexadecimal(cor_rgb):
        r_hex = decimal_para_hexadecimal(cor_rgb[0])
        g_hex = decimal_para_hexadecimal(cor_rgb[1])
        b_hex = decimal_para_hexadecimal(cor_rgb[2])

        # r_hex = hex(cor_rgb[0]).strip('0x').upper()
        # g_hex = hex(cor_rgb[1]).strip('0x').upper()
        # b_hex = hex(cor_rgb[2]).strip('0x').upper()

        return f"#{r_hex.zfill(2)}{g_hex.zfill(2)}{b_hex.zfill(2)}"

    cor_rgb = rgb_hexadecimal_para_decimal(cor_em_hexadecimal)
    cor_hexadecimal = rgb_decimal_para_hexadecimal(cor_rgb)
    print(f"Cor em hexadecimal: {cor_hexadecimal}")

    return f"rgb({cor_rgb[0]}, {cor_rgb[1]}, {cor_rgb[2]})"

def main():
    cor_hex = input("Digite a cor em hexadecimal (ex: #FF5733): ")
    resultado = conversao_rgb(cor_hex)
    print(resultado)

if __name__ == "__main__":
    main()