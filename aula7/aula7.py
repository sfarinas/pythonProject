"""
FSTRING
"""

nome = 'Salomao'
idade = 42
altura = 1.89
e_maior = idade > 18
peso = 80
imc = peso // (altura ** altura)
teste = """ ISSO é uma teste """

print('O ', nome, ' tem ', idade, ' idade ', ' e  com ', altura, ' altura, gostaria de saber se é maior de idade ', e_maior)

print('Seu IMC é = ', imc, teste)
# COMO USAR FSTRING
print(f'O {nome} tem {idade} idade, e com {altura} altura, gostaria de saber se é maior de idade {e_maior}')
print(f'Seu IMC é = {imc}')

#print('{} tem {} anos e com {} altura, gostaria de saber se é maior de idade {}'.format(nome, idade, altura))
print('{} tem {} anos e pesa {}'.format(nome, idade, peso))
print('{0} tem {1} anos e pesa {2}'.format(nome, idade, peso))
print('{0} tem {1} anos tem {3} de altura, e de maior {4} e seu IMC esta {5}'.format(nome, idade, imc, altura, e_maior, imc))
print('{n} tem {i} anos e pesa {p}'.format(n=nome, i=idade, p=peso))


#print('Seu IMC é '.format(imc))