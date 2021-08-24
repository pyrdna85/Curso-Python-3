"""
Variáveis: Podem iniciar com letras, conter números, seperar com _ e conter letras minusculas
"""

nome = str(input('Seu nome: '))
altura = float(input('Sua altura: '))
peso = float(input('Seu peso: '))
imc = peso / altura** 2
print(f'Olá {nome}, seu IMC é de {imc:.1f}')


