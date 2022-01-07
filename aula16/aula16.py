"""
Manipulando strings - Aula 6
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funçoes built-in len, abs, type, print, etc ...
Essas funçoes podem ser usadas diretamente em cada tipo.

Voce pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""
#  INDICES
#  positivos    [012345678]
texto         = 'Python-s2'
#  Negativos   -[987654321]

print( texto[5] )
nova_string = texto[2:6]
print(nova_string.title())
nova_string = texto[0::2]
print(nova_string)

for letra in texto:
    print(letra)
print()  # pular linha
#
url = 'www.google.com/'
for ulr in url[:-1]:
    print(ulr)
print( url[:-1] )
