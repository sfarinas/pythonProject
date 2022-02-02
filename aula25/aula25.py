"""
Desempacotamento em PYTHON
"""
lista = ['Luiz', 'Maria', 'Joao',1,2,3,4,5,6,7,8,9,100]

n1, n2, *outra_lista = lista

print(n2, outra_lista)

#  PARA IMPRIMIR O ULTIMO VALOR
n1, n2, *outra_lista, ultimo = lista

print(ultimo)




