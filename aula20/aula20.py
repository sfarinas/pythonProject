"""
For in em Python
iterando string com for
Funçao range (start = 0, stop, step = 1)
"""

texto = 'Python'

for n, letra in enumerate(texto):
    print(n, letra)

nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

    print(nova_string)