"""
Operadores Logicos
and, or, not
in e not in
"""
"""
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = input('Digite o ultimo numero: ')

comp1 = n1 and n2
comp2 = n1 and n3
print(comp1)

if comp1 == True:
    print(f'comp1 é {comp1} verdadira ')
else:
    print(f'A comp1 {comp1} por isso é falsa')

if comp2 == True:
    print(f'comp2 é {comp2} verdadeira ')
else:
    print(f'A comp2 {comp2} por isso é falsa')
"""

nome = 'Salomao'
n1 = 1
n2 = 2
print('########################## in #####################')
if 'o' in nome:
    print(f'Existe {nome}')
else:
    print('nao existe')
print('########################## and #####################')
if n1 <= n2 and n1 != nome:
    print('Verdadeiro em and')
else:
    print('falso em and')
print('########################## or #####################')
if n1 > n2 or n2 != nome:
    print('Verdadeiro em or')
else:
    print('Falso em or')