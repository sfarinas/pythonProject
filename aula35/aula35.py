# A variavel criada fora de uma funcao

variavel = 'valor'


# Agora vamos criar dentro de uma funçao
def func():
    print(variavel)

def func2():
    variavel = 'Outro Valor'
    print(variavel)

func()
func2()
print()
# Aqui conseguimos ver que a variavel dentro da funcao é outra, totamente diferente.
# Por mais que tenha o mesmo nome, sao variaveis diferentes
print(variavel)

def linha():
    print()
    print('======PPPPP======U====U====L============================================================')
    print('======P====P=====U====U====L============================================================')
    print('======PPPPP======U====U====L============================================================')
    print('======P==========U====U====L============================================================')
    print('======P===========UUUU=====LLLLLLL======================================================')
    print()

# Alterando uma variavel global de dentro de uma funcao
linha()

def func3():
    global variavel
    variavel = 'Novo Valor'
    #print(variavel)
print(variavel)






