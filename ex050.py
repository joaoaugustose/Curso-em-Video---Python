soma = 0
cont = 0

for i in range (1, 7):
    num = int(input('Informe um número inteiro: '))

    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1

print('A soma dos {} números informados é {}'.format(cont, soma))

'''soma = 0
cont = 0
for i in range (1, 7):
    num = int(input('Informe um numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares, somando eles da {}'.format(cont, soma))'''
