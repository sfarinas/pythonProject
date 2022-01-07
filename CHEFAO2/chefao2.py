"""
Faca um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario nao digite um numero
inteiro, informe que nao é numero inteiro.
"""
print('=============== PRIMEIRO EXERCICIO =================')
print('Faca um programa que peça ao usuario para digitar um numero inteiro,')
print('informe se este numero é par ou impar. Caso o usuario nao digite um numero')
print('inteiro, informe que nao é numero inteiro.')
print()

n1 = input('Digite um numero inteiro: ')
if not n1.isdigit():
    print('DIGITE UM NUMERO VALIDO')
else:
    n1 = int(n1)

    if n1 % 2 == 0 and n1 != 0:  #  checagem de numero par
        print(f'{n1} = Numero é par')
    elif n1 != 0:
        print(f'{n1} = Numero é impar')
    else:
        #if n1 == 0:
            print('zero é neutro')




"""
Faça um programa que pergunte a hora ao usuario e , baseando-se no horario descrito,
exiba a saudacao apropriada. 
EX: Bom dia 0-11, tarde 12-17, noite 18-23.
"""
print()
print('=============== SEGUNDO EXERCICIO =================')
print('Faça um programa que pergunte a hora ao usuario e , baseando-se no horario descrito,')
print('exiba a saudacao apropriada.')
print('EX: Bom dia 0-11, tarde 12-17, noite 18-23.')
print()

hora = input('Qual a hora agora: ')

#if not n1.isdigit() or not n2.isdigit():
if hora.isdigit():
    hora = int(hora)
    if hora <= 11:
        print('Bom dia')
    elif hora <= 17:
        print('Boa tarde ')
    elif hora <= 23:
        print('Boa noite!')
    else:
        print('Digite um numero valido')
else:
    print('ENTRE COM VALOR VALIDO')


"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
print('=============== TERCEIRO EXERCICIO =================')
print('Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras')
print('ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva')
print('"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".')
print()

nome3 = input('Digite seu nome: ')
qtd_cara = len(nome3)

if qtd_cara <= 4:
    print(f'O nome {nome3} é curto')
elif qtd_cara >= 5 and qtd_cara <=6:
    print('Seu nome é normal.')
elif qtd_cara > 6:
    print('Seu nome é muito grande!')