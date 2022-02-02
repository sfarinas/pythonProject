"""
Funcoes - def em Python - return - ( parte 2 )
"""
def msgPadrao():
    print()
    print('------  MENSAGEM PADRAO PARA SEPARAR MATERIAL  --------')
    print()


def funcao(var):
    return var

variavel = funcao('Valor que eu quero ')

if variavel:
    print(variavel)
else:
    print('Nenhum valor. ')

msgPadrao()

def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8,4)

if divide:
    print(divide)
else:
    print('Conta Invalida. ')

msgPadrao()

def dumb():
    return ('Luiz','Otavio')

var = dumb()

print(var,type(var))

msgPadrao()

def teste():
     nomee = input('Digite um nome: ')
     nomee2 = input('Digite qual quer coisa: ')
     return nomee,nomee2
teste()
far = teste()
print(far,type(far))
