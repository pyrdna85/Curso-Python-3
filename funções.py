"""
Funções - def em Python (Parte1)
def funcao(msg='Ola', nome='usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'


print(funcao)
"""

"""
Funções - def em Python (Parte2)
def funcao(var):
    return var

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('nenhum valor.')
    
    
def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2

calculo = divisao (8, 4)

if calculo:
    print(calculo)
else:
    print('Operação inválida')

"""

"""
Exercícios Função
1 - Crie uma função que exibe uma saudação com os parêmetros saudação e nome.
nome = input('Digite seu nome: ')
def saudacao():
    return (f'Olá {nome}, seja bem vindo')

var = saudacao()
print(var)

2 - Crie uma função que receba 3 núemros como parâmetros e exiba a soma entre eles
cont = 0
for c in range(3):
    numero = int(input('Informe um número: '))
    cont += numero

def soma():
    return cont
var = soma()
print(var)

3 - Crie uma função que receba dois números. O primeiro é um valor e o segundo um percentual (ex. 10%).
Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.
cont = 1
lista = []
while cont >= 0:
    numero = int(input('Informe um número: '))
    lista.append(numero)
    cont -= 1
a = lista[0]
b = lista[1] / 10

def calculo():
    return a + b

var = calculo()
print(var)

"""




