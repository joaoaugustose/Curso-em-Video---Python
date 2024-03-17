soma = 0
cont = 0

for i in range(0, 500, 3):

    if i % 2 == 0:
        var = 0

    else:
        cont = cont + 1
        soma = soma + i

print('A soma dos {} números é {}.'.format(cont, soma))