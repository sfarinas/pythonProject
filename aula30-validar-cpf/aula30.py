"""  FORMULA
CPF = 168.995.350-09
----------------------------------------
1 * 10 = 10             #   1 * 11 = 11 <-
6 * 9 = 54              #   6 * 10 = 60
8 * 8 = 64              #   8 *  9 = 72
9 * 7 = 63              #   9 *  8 = 72
9 * 6 = 54              #   9 *  7 = 63
5 * 5 = 25              #   5 *  6 = 30
3 * 4 = 12              #   3 *  5 = 15
5 * 3 = 15              #   5 *  4 = 20
0 * 2 = 0               #   0 *  3 = 0
                        #   0 *  2 = 0
        297             #           343
11 - (297 % 11) = 11    #      11 - (343 % 11) = 9
11 > 9 = 0              #
Digito 1 = 0            #       digito 2 = 9

"""

while True:
    # cpf = '16899535009'
    cpf = input('Digite seu CPF: ')
    novo_cpf = cpf[:-2]                 # Elimina os dois ultimos digitos do CPF.
    reverso = 10                        # Contador reverso
    total = 0
    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro indice vai de 0 a 9
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso     # Valor total da multiplicação

        reverso -= 1                    # Decrementa o conteudo reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)
    # Evita sequencias. EX: 11111111111, 00000000000 ...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    reverso -= 1
    if cpf == novo_cpf:
        print('Valido')
    else:
        print('Invalido')
