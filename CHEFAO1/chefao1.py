nome1 = 'Gustavo'
nome2 = 'Sara'
nome3 = 'Simone'
idade1 = 30
idade2 = 25
altura1 = 1.78
altura2 = 1.87
ano = 2011
ano2 = 2016
peso = 74.4
peso2 = 78.7
imc = peso // (altura1 ** altura1)
imc2 = peso2 // (altura2 ** altura2)
#########   GUSTAVO
print('{n1} filho de {n3}, irmao de {n2}, tem {a} de altura de barriga, seu IMC é {im} e nasceu no ano {no}'
      .format(n1=nome1, n2=nome2, n3=nome3, i=idade1, a=altura1, no=ano, im=imc))
######### SARA
print('{n2} filho de {n3}, irmao de {n1}, tem {a} de altura, seu IMC é {im} e nasceu no ano {no}'
      .format(n1=nome1, n2=nome2, n3=nome3, i=idade1, a=altura2, no=ano2, im=imc2))

print('"ja sei "')