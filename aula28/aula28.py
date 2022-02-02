"""
EXPRESSAO CONDICIONAL OPERADOR OR
"""
nome = input('Qual seu nome? ')

if nome:
    print(nome)
else:
    print('Voce nao digitou nada =(')

print()
#  JEITAO DO PYTHON
print('#  JEITAO DO PYTHON')

nome1 = input('Digite outro nome? ')
print(nome1 or 'Voce nao digitou nada! ')