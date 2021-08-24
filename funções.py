"""
Funções - def em Python (Parte1)
def funcao(msg='Ola', nome='usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'


print(funcao)
"""

"""
Funções - def em Python (Parte2)
"""

def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

divide = divisao(8,2)

if divide:
    print(divide)
else:
    print('Operação inválida')
