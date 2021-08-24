frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
print(tamanho_frase)
nova_string = ''
cont = 0
maiusc = input('Qual letra deve ficar maiúscula?: ')

while cont < tamanho_frase:
    letra = frase[cont]
    if letra == maiusc:
        nova_string += maiusc.upper()
    else:
        nova_string += letra
    cont += 1

print(nova_string)