"""
OPERADORES TERNARIO
"""

logged_user = False

if logged_user:
    msg = 'Usuario logado.'
else:
    msg = 'Usuario precisa logar.'

print(msg)

#  Geito em python
print('Geito python')
msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar'
print(msg)



