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

4 - Fizz Buzz - Se o parâmentro da função for divisível por 2, retorne fizz, se o parâmentro da 
função for divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, 
retorne FizzBuzz, caso contrário, retorne o número enviado.


def fb(n):
    if n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    elif n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    else:
        return n
print(fb(10))
"""






