"""
Lista em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
lista = ['Indio','Homem','Gato','Faca','Elefante','Dado','Casa','Bola','Abelha']
string = 'IHGFEDCBA'
print('================= Apredendo lista 1 ============')
indice = input('Escolha um indice: ')
if indice.isnumeric():
    print(f'mostrar a lista no indice {indice} : ', lista[int(indice)])
    print(f'mostar a string no indice {indice}: ', string[int(indice)])
else:
    print('Digite um numero valido.')
print()
print('============= aprendendo lista 2 - EXTEND ============')
l1 = [1,2,3]
l2 = [2,3,4]
l3 = l1 + l2
print(f'Lista l1 = {l1} normal')
print(f'Lista l2 = {l2} normal')
print(f'Lista l3 = {l3}, soma da l1 + l2')

l1.extend(l2)
print(f'Lista l1 = {l1}, com extend da l2')
print()
print('============= aprendendo lista 3 - APPEND ============')
l1 = [1,2,3]
l2 = [2,3,4]
l2.append('LOLA')
print(f'Lista l2 no indice 3 é ',l2[3])
print()

print('============= aprendendo lista 4 - INSERT ============')
l2 = [2,3,4]

l2.insert(0,'Banana')
print(f'Lista l2, inserido ', l2[0],' No indice 0')
print()

print('============= aprendendo lista 5 - POP ============')
l2 = [4,5,6]
print(l2)
l2.pop()
print(l2)
print()

print('============= aprendendo lista 6 - DEL ============')
l2 = [1,2,3,4,5,6,7,8,9]
l2.insert(0,'Banana')
print(l2)
del (l2[0])
print(l2)
print()

print('============= aprendendo lista 7 - MAX e MIN ============')
l2 = [91,22,35,41,15,56,27,88,49]

print(max(l2))
print(min(l2))
print()

print('============= aprendendo lista 8 - RANGE ============')
l2 = list(range(0,100,4))
print(l2)
for valor in l2:
    print(valor)
print()


