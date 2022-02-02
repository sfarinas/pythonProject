"""'
------- DICIONARIO --------
"""
d1 = {'chave1':'Valor da chave'}

print(d1)

d1['chave2'] = 'valor chave 2'
print(d1)
print(d1['chave2'])

n1 = 0
n1 = n1 + 1
d1 [n1] = 'novo valor'
print(d1)

""""
-- CRIANDO UMA COPIA DO DICIONARIO, E EDITANDO O INDICE NA COPIA
"""
d1 = { 1: 'a', 2: 'b', 3: 'c', 4: 'simona'  } # CRIANDO UM DICIONARIO
v = d1.copy() # CRIANDO UMA COPIA
v[1] = 'simchat' # ALTERANDO O INDICE 1

print(d1)  # VENDO A DIFERENÇA
print(v)   # VENDO A DIFERENÇA

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d2 = dict(lista)
print(d2)



