"""
Listas em Python: https://docs.python.org/pt-br/3/tutorial/datastructures.html
"""

secreta = 'papelao'
digitados = []
contador = len(secreta) + 3

while True:
    letra = input(f'Você {contador} tentativas. Digite uma letra: ')
    contador -= 1

    if letra in secreta:
        print(f'A letra {letra} existe na palavra secreta.')
        digitados.append(letra)
    else:
        print(f'A palavra {letra} não está na palabra secreta.')

    secreto_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    print(secreto_temporario)
    if secreto_temporario == secreta:
        print(f'Parabéns, você acertou. A palavra é: {secreta}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if contador == 0:
        print(f'Suas tentativas acabaram. Você perdeu. A palavra era {secreta}')
        break






