"""
Slipt, Join Enumerate: https://docs.python.org/3/library/functions.html
Split: Dividir uma string
Join: Juntar uma lista
Enumerate: Enumerar elementos da lista
"""

string = 'Florida é a minha próxima morada, vou morar lá com a minha familia.'
lista1 = string.split(' ')
lista2 = string.split(',')

print(lista1)
print(lista2)



for valor in lista1:
    print(f'{valor} apareceu {lista1.count(valor)}x na frase.')



