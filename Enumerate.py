"""
Enumerate - Enumerar elementos da lista
"""

lista = [
        ['Edu', 'João', 'Luiz'],
        ['Pedro', 'Maria', 'Cris'],
        ['Jussara', 'Isabela', 'Laura'],
]

enumerada = list(enumerate(lista))
print(enumerada[1][1][0])

