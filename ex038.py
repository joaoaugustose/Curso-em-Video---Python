#ler 2 números inteiro e comparar:
#Se o primeiro numero é maior
#Se o segundo numero é maior
#Se os numeros são iguais

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

if n1 > n2:
    print('O número {} é maior que o número {}.'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que o número {}.'.format(n2, n1))
else:
    print('Os números informados são iguais!')
