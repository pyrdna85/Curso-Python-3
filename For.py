"""
For in em Python: Iterando strings com for - Função range(start=0, stop, step=1)
"""
cont = 0
tabuada = int(input('Digite uma tabuada: '))
for x in range(1 ,11):
    cont += 1
    print(f'{tabuada} x {x} = {tabuada * x}')

for c in range(0, 100, 8):
    print(c)

print()

for d in range(100):
    if d % 8 == 0:
        print(d)


texto = 'Python'
nova_string = ''
diga = input('Letra 1: ')
digb = input('Letra 2: ')


for letra in texto:
    if letra == diga:
        nova_string += letra.upper()

    elif letra == digb:
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
