""""""
"""
FUNCAO (def) EM PYTHON - *args **kwargs - 
"""
from random import randint
def func(*args):
    print(args)

    # for v in args:
    #     print(v)

    # print('Todos ')
    # print(args)
    # print('Somente o primeiro ')
    # print(args[0])
    # print('Somente o Ultimo ')
    # print(args[-1])
    # print('Contagem de todos ')
    # print(len(args))

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista + lista2)
func(*lista, *lista2)

# func(1,2,3,4,5)

# lista = [1,2,3,4,5]
# print(*lista, sep='-')
# print()


