"""
For / else
"""
variavel = ['Salomao', 'Simone', 'filhos']

for valor in variavel:
    print(valor)
    print(valor)
    break

for valor in variavel:
        if valor.lower().startswith('s'):
            print('Começa com S ',valor)
        else:
            print('Nao comeca com S ', valor)

comeca_com_s = False

for valor in variavel:
    if valor.startswith('S'):
        comeca_com_s = True

if comeca_com_s:
    print('Existe uma palavra que começa com S. ')
else:
    print('Nao existe uma palavra que começa com S. ')


