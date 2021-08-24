nota1 = float(input('digite a nota da sua primeira prova: '))
nota2 = float(input('digite a nota da sua segunda prova: '))

media = 8

calculo = (nota1 + nota2) / 2

if calculo > media:
    print('aprovado')
    print(calculo)
else:
    print('reprovado')
    print(calculo)
