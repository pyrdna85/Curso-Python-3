"""
Desempacotamento de listas e Python
"""

lista = ['Luiz', 'Joao', 'Marcos',1,2,3,4,5,6,7,8,9, 'ultimo']

n1, n2, *outraLista, ultimo = lista

print(n2, outraLista, ultimo)