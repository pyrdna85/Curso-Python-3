"""
* Criar variáveis para nome (str), indade(int),
* altura (float) e peso (float) de uma pessoa
* Crtiar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos o valores na tela usadno F-String (com as chaves)
"""

nome = str(input('Nome: '))
idade = int(input('Idade: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / altura ** 2
data = 2021 - idade
print(f'{nome} tem {idade} e {altura} altura')
print(f'O IMC de {nome} é de {imc:.2f}')
print(f'{nome} nasceu em {data}')

