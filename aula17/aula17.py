"""
while em Python - Aula 7
utilizado para realizar acoes enquanto
uma condicoes for verdadeira.

Requesitos: Entender condicoes e operadores
"""
x = 0
while x < 20:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1

x = 0
while x < 20:
    if x == 3:
        x = x + 1
        break
    print(x)
    x = x + 1

#  Planilha
x = 0   # coluna
while x < 10:
    y = 0   # linha

    while y < 5:
        print(f'{x},{y}')
        y += 1
    x +=1
print('ACABOU')


while True:
    nome = input('Qual o seu nome: ')
    print(f'Ola ')

