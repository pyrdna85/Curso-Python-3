"""
cpf = [3, 6, 5, 6, 4, 3, 4, 0, 8, 5, 0]
remocao = cpf[:9]

contador = 11
acumulador = 0
for c in remocao:
    contador -= 1
    resultado = c * contador
    acumulador = acumulador + resultado
    print(f'{c} * {contador} = {resultado}')

calculo = 11 - (acumulador % 11)
if calculo > 9:
    remocao.append(0[:9])
print(remocao)
print(calculo)
print(acumulador)
"""

for index in range (19):
    print('Oi')



