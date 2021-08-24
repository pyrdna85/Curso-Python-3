"""
Formatando valores com modificadores

:s - texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
: (CARACTERE)(> ou < ou )(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direira
^ - Centro
"""

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 2
print(f'{num_2:0^9}')

nome_1 = 'rodrigo Andrade'
nome_2 = 'Carla Lima'

print(nome_1.lower())
print(nome_1.upper())
print(nome_1.title())

print('{0} {1}'.format(nome_1, nome_2))