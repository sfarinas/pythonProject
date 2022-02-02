perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2+2 ?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 3*2 ?',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}
print()
respostas_certas = 0

#  AQUI VC MONTA AS PERGUNTAS
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    #  AQUI VC MONTA O VISUAL DO QUIZ
    print('Respostas: ')
    for rk, rv in pv [ 'respostas'].items():
        print(f'[ {rk} ]: {rv}')

    #  ENTRADA DA RESPONTA DO USUARIO
    resposta_usuario = input('Sua resposta: ')

    # AQUI COMPARA O QUE O USUARIO DIGITOU COM O QUIZ
    if resposta_usuario == pv[ 'resposta_certa']:
        print('Voce acertou! ')
        respostas_certas += 1
    else:
        print('Voce Errou. ')
    print()






