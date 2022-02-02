"""
1 - Crie uma funçao que exibe uma saudacao com os parametros saudacao e nome.
"""
print('1 - Crie uma funçao que exibe uma saudacao com os parametros saudacao e nome.')

def funcao(saudacao, nome):
    print(saudacao,nome)
funcao('Ola ', 'Salomao')
print()
"""
2 - Crie uma funcao que receba 3 numeros como parametros e exiba a soma entre eles. 
"""
print('2 - Crie uma funcao que receba 3 numeros como parametros e exiba a soma entre eles. ')
def soma(n1, n2, n3):
    print(n1+n2+n3)
soma(1,2,3)
soma(3,4,5)
print()

"""
3 - Crie uma funcao que receba 2 numeros. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return) o valor do primeiro numero somado do aumento do percentual do mesmo.
"""
print('3 - Crie uma funcao que receba 2 numeros. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return)')

def aumento_percentual(valor, percentual):
    #print(valor + (valor * percentual / 100))
    return valor + (valor * percentual / 100)

ap = aumento_percentual(50,10)
print(ap)
ap = aumento_percentual(100,10)
print(ap)
print()

""" 
4 - Fizz Buzz - Se o parametro da funcao for divisivel por 3, retorne fizz,
se o parametro da funcao for divisivel por 5, retorne buzz. 
Se o paramentro da funcao for divisivel por 5 e por 3, retorne FizzBuzz, caso contrario, retorne o numero enviado.
"""
print(
    '4 - Fizz Buzz - Se o parametro da funcao for divisivel por 3, retorne fizz,'
    'se o parametro da funcao for divisivel por 5, retorne buzz. '
    'Se o paramentro da funcao for divisivel por 5 e por 3, retorne FizzBuzz, caso contrario, retorne o numero enviado.'
)
def fb (n):
    if n % 3 == 0 and n % 5 == 0:
        return f'FizzBuzz, {n} é divisivel por 3 e 5'
    elif n % 5 == 0:
        return f'Buzz, {n} é divisivel por 5'
    elif n % 3 == 0:
        return f'Fizz, {n} é divisivel por 3'
    else:
        return n

print(fb(15))

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))


