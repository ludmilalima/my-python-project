def codificar_mensagem(mensagem, deslocamento):
    mensagem_codificada = ""
    for char in mensagem:
        # aplicar deslocamento para letras maiúsculas
        if (65 <= ord(char) <= 90):
            valor_ascii_pre = ord(char)
            posicao_no_alfabeto_pre_deslocamento = valor_ascii_pre - ord('A')
            posicao_no_alfabeto_pos_deslocamento = (posicao_no_alfabeto_pre_deslocamento + deslocamento) % 26
            valor_ascii_pos = posicao_no_alfabeto_pos_deslocamento + ord('A')
            mensagem_codificada += chr(valor_ascii_pos)
        # aplicar deslocamento para letras minúsculas
        elif (97 <= ord(char) <= 122):
            valor_ascii_pre = ord(char)
            posicao_no_alfabeto_pre_deslocamento = valor_ascii_pre - ord('a')
            posicao_no_alfabeto_pos_deslocamento = (posicao_no_alfabeto_pre_deslocamento + deslocamento) % 26
            valor_ascii_pos = posicao_no_alfabeto_pos_deslocamento + ord('a')
            mensagem_codificada += chr(valor_ascii_pos)
        # manter outros caracteres inalterados
        else:
            mensagem_codificada += char
    return mensagem_codificada

def decodificar_mensagem(mensagem_codificada, deslocamento):
    mensagem_decodificada = ""
    for char in mensagem_codificada:
        # aplicar deslocamento inverso para letras maiúsculas
        if (65 <= ord(char) <= 90):
            valor_ascii_pre = ord(char)
            posicao_no_alfabeto_pre_deslocamento = valor_ascii_pre - ord('A')
            posicao_no_alfabeto_pos_deslocamento = (posicao_no_alfabeto_pre_deslocamento - deslocamento) % 26
            valor_ascii_pos = posicao_no_alfabeto_pos_deslocamento + ord('A')
            mensagem_decodificada += chr(valor_ascii_pos)
        # aplicar deslocamento inverso para letras minúsculas
        elif (97 <= ord(char) <= 122):
            valor_ascii_pre = ord(char)
            posicao_no_alfabeto_pre_deslocamento = valor_ascii_pre - ord('a')
            posicao_no_alfabeto_pos_deslocamento = (posicao_no_alfabeto_pre_deslocamento - deslocamento) % 26
            valor_ascii_pos = posicao_no_alfabeto_pos_deslocamento + ord('a')
            mensagem_decodificada += chr(valor_ascii_pos)
        # manter outros caracteres inalterados
        else:
            mensagem_decodificada += char
    return mensagem_decodificada

def imprimir_caracteres(mensagem_decodificada, mensagem_codificada):
    for letra in range(0, len(mensagem_decodificada)):
        print(f"{mensagem_decodificada[letra]} - {ord(mensagem_decodificada[letra])} -> {mensagem_codificada[letra]} - {ord(mensagem_codificada[letra])}")

if __name__ == "__main__":
    mensagem = "Minha terra tem palmeiras,\nOnde canta o sabiá;\nAs aves, que aqui gorjeiam,\nNão gorjeiam como lá.\nNosso céu tem mais estrelas,\nNossas várzeas têm mais flores,\nNossos bosques têm mais vida,\nNossa vida mais amores.\nEm cismar, sozinho, à noite,\nMais prazer encontro eu lá;\nMinha terra tem palmeiras,\nOnde canta o sabiá."
    deslocamento = 3

    mensagem_codificada = codificar_mensagem(mensagem, deslocamento)
    print(f"Mensagem codificada:\n {mensagem_codificada}\n")

    mensagem_decodificada = decodificar_mensagem(mensagem_codificada, deslocamento)
    print(f"Mensagem decodificada:\n {mensagem_decodificada}\n")

    imprimir_caracteres(mensagem_decodificada, mensagem_codificada)
