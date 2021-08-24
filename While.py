"""
While em Python: utilizado para realizar ações enquanto uma condição
for verdadeira

Requisitos: Entender condições e operações

x = 0
while x < 10:

    if x == 5:
        x += 1
        break
    print(x)
    x += 1
print('acabou')


x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'{x},{y}')
        y += 1
    x += 1
print('Fim do programa')
"""
while True:
    print()
    calc_1 = input('Digite um número: ')
    calc_2 = input('Digite outro número: ')
    operador = input('Digitwe um operador [+ - * /]: ')
    sair = input('Digite [C] para calcular ou [S] para sair').upper()

    if sair == 'S':
        break

    if not calc_1.isnumeric() or not calc_2.isnumeric():
        print('Você precisa digitar um número')
        continue


    calc_1 = int(calc_1)
    calc_2 = int(calc_2)

    if operador == '+':
        print(calc_1 + calc_2)
    elif operador == '-':
        print(calc_1 - calc_2)
    elif operador == '*':
        print(calc_1 * calc_2)
    elif operador == '/':
        print(calc_1 / calc_2)