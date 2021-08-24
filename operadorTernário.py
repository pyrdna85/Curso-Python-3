"""
Operador ternário em Python
"""

idade = input('Qual é sua idade? :')

if not idade.isnumeric():
    print('Você precisa digitar um número')
else:
    idade = int(idade)
    maior = (idade >= 18)
    msg = 'Logado' if maior else 'Deslogado'

    print(msg)