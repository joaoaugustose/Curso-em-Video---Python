#fazer um programa q leia 3 numeros e identifique o maior e o menor
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

maior = n1
menor = n3

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O número maior digitado é o {}.'.format(maior))

if n1 < menor:
    menor = n1
if n2 < menor:
    menor = n2
print('O número menor digitado é o {}'.format(menor))
