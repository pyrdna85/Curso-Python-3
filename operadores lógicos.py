"""
Operadores lógicos
and, or, not, in e not in
"""

usuario = input('Nome de usuário: ')
senha = input('Senha do usuario: ')

usuario_db = 'pyrdna85'
senha_bd = 'mnxh2326'

if usuario_db == usuario and senha_bd == senha:
    print('Logado')
else:
    print('Verifique seus dados')