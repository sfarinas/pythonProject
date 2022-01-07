ctr = 0
while True:
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    op = str(input('soma +, dimi -, multi *, div /, potenci **, resto da divi // : '))
    print()
    print('VAMOS VER A DIFERENÇA ENTRE')
    print('# isnumeric # isdigital # isdecimal')
    print()

    if not n1.isdigit() or not n2.isdigit():
        print('Digite um numero valido ')

    else:
         n1 = int(n1)
         n2 = int(n2)

         if op == '+':
            print(f'{n1} + {n2} ')
            print(n1 + n2)
         elif op == '-':
            print(f'{n1} - {n2} ')
            print(n1 - n2)
         elif op == '*':
             print(f'{n1} * {n2} ')
             print(n1 * n2)
         elif op == '/':
             print(f'{n1} / {n2} ')
             print(n1 / n2)
         elif op == '**':
             print(f'{n1} ** {n2} ')
             print(n1 ** n2)
         elif op == '//':
             print(f'{n1} // {n2} ')
             print(n1 // n2)
         elif op == ' ':
             print('VOCE DIGITOU ESPAÇO EM BRANCO')
         elif op == 'X' or op == 'x':
             break

         else:
             print(f'{op} NÃO É UM VALOR VALIDO ')

    ctr += 1
