"""
Operador Relacionais - aula 10
== > >=  < <= !=
"""
print('Comparacao de valor')
n1 = 2
n2 = 2
# num sera True ou False
num =  n1 == n2
if num == True:
    print('Valor realmente é 2')
else:
    print('Valor é diferente de 2')
print()

print('brincando com int e str')
n1 = input('digite um numero : ')
n2 = int(input('digite outro numero: '))

print('Essa linha sera falso : ', n1 == n2, ' Nao tera soma e sim uniao que é : ', n1 + str(n2))
print('Esse linha sera verdadeiro : ', int(n1) == n2, ' Pois a soma dos numero é : ', int(n1) + n2)
# Dara sempre falso, por que n1 é str
num = n1 == n2

if num == True:
    print('Se entrou aqui é por que era verdadeiro : ', num)
else:
    print('Aqui so entra quando é falso : ', num)
# Aqui sempre sera verdadeiro
print()
num = int(n1) == n2

if num == True:
    print('Se entrou aqui é por que era verdadeiro : ', num)
else:
    print('Aqui so entra quando é falso : ', num)

