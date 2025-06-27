dicionario_morse = {
    'A': ".-",
    'B': "-...",
    'C': "-.-.",
    'D': "-..",
    'E': ".",
    'F': "..-.",
    'G': "--.",
    'H': "....",
    'I': "..",
    'J': ".---",
    'K': "-.-",
    'L': ".-..",
    'M': "--",
    'N': "-.",
    'O': "---",
    'P': ".--.",
    'Q': "--.-",
    'R': ".-.",
    'S': "...",
    'T': "-",
    'U': "..-",
    'V': "...-",
    'W': ".--",
    'X': "-..-",
    'Y': "-.--",
    'Z': "--..",
    '0': "-----",
    '1': ".----",
    '2': "..---",
    '3': "...--",
    '4': "....-",
    '5': ".....",
    '6': "-....",
    '7': "--...",
    '8': "---..",
    '9': "----.",
    ' ': " " # o prof não incluiu espaço na lista mas o resultado dele contém 1 espaço entre as palavras 'Hello' e 'World' 
}

def converter_codigo_morse(mensagem):
    mensagem_convertida = ''
    index = 0
    for char in mensagem:
        value = dicionario_morse.get(char.upper(), '')
        if value != '':
            index += 1
            mensagem_convertida = (mensagem_convertida + dicionario_morse.get(char.upper(), '') + ' ')
            print(f"{mensagem[0:index]} -> {mensagem_convertida}")

converter_codigo_morse('Hello, World!')