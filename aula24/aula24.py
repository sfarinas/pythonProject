"""
* Enumerate  -  Enumerar elementos da lista # list
"""
nomes = 'Edu', 'Silmara', 'Joao'
nomes1= 'Samara', 'Saulo', 'Pedro'

lista = [
    [nomes[1], nomes[0], nomes[2]],
    [nomes1[2], nomes1[0], nomes1[1]]
        ]

lista2 = [
    ['Salomao', 'Simone', 'carro'],
    ['Helen', 'Ed', 'Lu'],
    ['Kaka', 'Rivaldo', 'Ronaldo']
        ]
enumerada = list(enumerate(lista2))
print(enumerada[0][1][0])   #  resposta= Salomao
print()
for v1, v2 in enumerate(lista2, 20):
    print(v1, v2)

#print(lista)

#  GUSTAVO
print()
print('GUSTAVO')
for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)

#  SARA
print()
print('SARA')
for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)






