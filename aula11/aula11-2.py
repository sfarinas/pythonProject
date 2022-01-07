"""
Operadores Logicos
and, or, not
in e not in
"""

usuario = input('Nome de usuario: ')
senha = int (input('passowrd: '))
print()

if usuario == 'Salomao' and senha == 123:
    print(f'Acesso liberado {usuario}')
elif usuario != 'Salomao' and senha == 123:
    print('Usuario errada ')
elif usuario == 'Salomao' and senha != 123:
    print('Senha errada ')
else:
    print('Usuario e senha errados ')


