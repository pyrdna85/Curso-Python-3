# Exercício 01
num = input('Digite um número: ')

try:
    conv = int(num)
    if conv % 2 == 0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é impar')
except:
    print(f'Não e inteiro')

# Exercício 02
hora = input('Que horas são?: ')

if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('A hora informada deve estar entre 0 e 23.')
    else:
        if hora <= 11:
            print('Bom dia')
        elif hora >=12 and hora <=19:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('Por favor, digite um horário entre 0 e 23.')

# Exercício 3
nome = input('Informe seu primeiro nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print(f'O nome informado é curto')
elif tamanho >= 5 and len(nome) <= 6:
    print(f'O nome informado tem um tamanho normal')
elif tamanho > 6:
    print(f'O nome informado tem um tamanho muito grande')

