"""
Funcoes - def em Python ( parte 1 )
"""
def funcao(msg):
    print(msg)

funcao('Mensagem')
funcao('pra vc')

def saudacao (msg, nome):
    print(msg, nome)

saudacao('Ola', 'Salomao Farina')

print()
def ola(men = 'Ola', vc = 'Usuario'):
    print(men, vc)

ola()
ola('Oi', 'Como esta')

print()
def oi(msg = 'Oie', usuario = 'Voce que esta ai'):
    msg = msg.replace('a', '@')
    usuario = usuario.replace('o', '0')
    print(msg, usuario)

oi('')
oi('Ola', 'voce e eu somos oficiais')
oi('')
oi('')
print()
def saudacao (msg = 'Ola', nome = 'Salomao'):
    return f'{msg} {nome}'
variavel = saudacao()
print('Teste ',variavel)


