#        indices
#        0123456789......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < 34:
    print(frase[contador])
    #  montando nova string
    nova_string += frase[contador]
    # print(contador)
    contador +=1
print(nova_string)


print('==================== outra maneira =============')
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < 34:
    letra = frase[contador]

    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    #nova_string += frase[contador]
    #print(contador)
    contador +=1
print(nova_string)
