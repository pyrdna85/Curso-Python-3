"""
Condições IF, ELIF e ELSE
"""

if False: # 0 então ele ignora e continua
    print('Verdadeiro')
    print('teste teste2')
elif True : # 1 então ele executa e finaliza o processo
    print('Agora é verdadeiro')
    nome = input('QUal é o seu nome?')
    print(f'{nome}')
elif False:
    print('Mais uma verdadeira')
    print(22 + 22)
else:
    print('Não é verdadeiro')
    print('Olá')


