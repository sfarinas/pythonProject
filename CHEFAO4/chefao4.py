""""
                    CHEFAO 4
"""
""""
1 - Crie uma funcao1 que receba uma funcao2 como parametro e retorne o valor da funcao2 executada.
"""
# def ola_mundo():
#     return 'Ola mundo'
#
# def mestre(funcao):
#     return funcao()
#
# executando = mestre(ola_mundo)
#
# print(executando)

""""
2 - Crie uma funcao1 que receba uma funcao como parametro e retorne o valor da funcao2 executada.  Faça a funcao1 
executar duas funcoes que recebam um numero diferente de argumentos.
"""
def mestre (funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao, animal):
    return f'{ saudacao} {nome} {animal}'

executando = mestre(saudacao, 'Luiz', 'Bom dia', 'Cachorro')
print(executando)





