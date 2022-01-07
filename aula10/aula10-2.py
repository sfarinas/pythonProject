"""
Operador Relacionais - aula 10
== > >=  < <= !=
"""
nome = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))

idade_menor = 20
idade_maior = 70

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar')
else:
    print(f'{nome} NAO pode pegar ')


