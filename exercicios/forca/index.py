import random

# Dicionário com as palavras e suas respectivas categorias
palavras = {'python': 'linguagem de programação', 'programacao': 'área da informática',
            'computador': 'equipamento eletrônico', 'teclado': 'periférico de entrada',
            'mouse': 'periférico de entrada', 'monitor': 'periférico de saída'}

# Seleciona uma palavra aleatória do dicionário
palavra_secreta = random.choice(list(palavras.keys()))

# Cria uma lista para armazenar as letras já usadas
letras_usadas = []

# Define o número máximo de tentativas
max_tentativas = 6

# Loop principal do jogo
while True:
    # Imprime a palavra com os caracteres adivinhados e os espaços vazios
    palavra_atual = ''
    for letra in palavra_secreta:
        if letra in letras_usadas:
            palavra_atual += letra
        else:
            palavra_atual += '_'
    print('Palavra: ' + palavra_atual)

    # Pede ao jogador para adivinhar uma letra ou pedir uma dica
    jogada = input('Digite uma letra ou digite "dica" para receber uma dica: ').lower()

    # Verifica se o jogador pediu uma dica
    if jogada == 'dica':
        print('Categoria da palavra: ' + palavras[palavra_secreta])
        continue

    # Verifica se a jogada já foi usada
    if jogada in letras_usadas:
        print('Você já usou essa letra, tente outra!')
        continue

    # Adiciona a jogada à lista de jogadas usadas
    letras_usadas.append(jogada)

    # Verifica se a jogada está na palavra secreta
    if jogada in palavra_secreta:
        print('Boa! A letra "' + jogada + '" está na palavra!')
    else:
        print('Ops! A letra "' + jogada + '" não está na palavra.')
        max_tentativas -= 1
        if max_tentativas == 5: 
            print("        <._.>")
        if max_tentativas == 4: 
            print("        <._.>")
            print("          |")
            print("          |")
        if max_tentativas == 3: 
            print("        <._.>")
            print("          |--")
            print("          |")
        if max_tentativas == 2: 
            print("         <._.>")
            print("         --|--")
            print("           |") 
        if max_tentativas == 1: 
            print("        <._.>")
            print("        --|--")
            print("          |")
            print("           \ ") 
        if max_tentativas == 0: 
            print("         <._.>")
            print("         --|--")
            print("           |  ")
            print("          / \ ") 

    # Verifica se o jogador perdeu o jogo
    if max_tentativas == 0:
        print('Você perdeu! A palavra secreta era "' + palavra_secreta + '".')
        break

    # Verifica se o jogador acertou todas as jogadas
    acertou_todas_jogadas = True
    for letra in palavra_secreta:
        if letra not in letras_usadas:
            acertou_todas_jogadas = False
            break
    if acertou_todas_jogadas:
        print('Parabéns! Você acertou a palavra secreta "' + palavra_secreta + '".')
        break
