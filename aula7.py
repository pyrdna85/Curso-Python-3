"""
Formas diferentes de imprimir
"""
nome = str(input('Seu nome: '))
altura = float(input('Sua altura: '))
peso = float(input('Seu peso: '))
imc = peso / altura** 2
print(f'Olá {nome}, seu IMC é de {imc:.1f}')
print('Olá {}, seu IMC é de {:.2f}'.format(nome, imc))
print('Olá {n}, seu IMC é de {im}'.format(n=nome, im=imc))
print('Olá {0}, seu IMC é de {1} '.format(nome, imc))
