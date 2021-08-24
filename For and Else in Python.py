"""
For / Else em Python
"""

variavel = ['Rodrigo Andrade', 'Carla Lima', 'jiguel Lima']
check = False
for valor in variavel:
    if valor.upper().startswith('J'):
        check = True
if check:
    print('Existe uma palabra que começa com J.')
else:
    print('Nenhuma palavra com J.')
