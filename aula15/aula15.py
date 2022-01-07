"""
Formatando valores com modificadores - aula 5
:s - texto (strings)
:d - Inteiros (int)
:f - Numeros de ponto flutuantes (float)
:.(NUMERO)f - Quantidades de casas decimais (float)
:(CARACTERE)(> ou < ou ^) ( QUANTIDADE ) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

n1 = 10
n2 = 3
divisao = n1 / n2

print('{:.2f}'.format(divisao))  # Primeira opcao de formatacao
print(f'{divisao:.2f}')  #  Segunda opcao de formatacao

nome = 'Salomao'
sobrenome = 'Farina'
qualquer = 'casa do pApai'
print(f'{nome:s}')  #  uma opcao diferente

nun1 = 134
print(f'{nun1:0>10}')  # add 0 a esquerda:0>10
print(f'{nun1:0<31}')  # add 0 a direita
print(f'{nome:0^79}')  # add 0 a centro

nome_formatado = '{:@>20}'.format(nome)
print(nome_formatado)
nome_formatado = '{1} {2} {0}'.format(nome,sobrenome,qualquer)
print(nome_formatado)

print(qualquer.lower())
print(qualquer.upper())
print(qualquer.title())
print(qualquer.count('casa'))


