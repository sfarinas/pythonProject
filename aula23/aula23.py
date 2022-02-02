"""
split, join, enumerate em python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteraveis
"""
string = "O Brasil é o pais do futebol, o Brasil e penta"
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)


print()
for valor in lista_1:
    print(f'A palavra "{valor}" apareceu {lista_1.count(valor)}x na frase')

print()

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é "{palavra}" ({contagem}x)')

for valor in lista_2:
    print(valor.split())

string2 = 'A Thaina é Penta.'
lista = string.split(' ')
string2 = ','.join(lista)

for indice, valor in enumerate(lista):
    print(indice, valor)

