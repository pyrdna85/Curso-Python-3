"""
While / Else: contadores e acumuladores
"""

cont = 2
acum = 2

while cont <= 10:
    print(cont, acum)

    if cont > 5:
        break

    acum = acum + cont
    cont += 1
else:
    print('Fim')