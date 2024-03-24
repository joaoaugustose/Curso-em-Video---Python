n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

contpar = 0

tupla = (n1, n2, n3, n4)
#informa todos os números
print(f'Você digitou os valores {tupla}.')

#informa quantas vezes aparece o número 9
print(f'O número 9 aparece {tupla.count(9)} vez')

#informa se o número 3 consta, caso conste, informa a posição.
cont3 = tupla.count(3)
if cont3 > 0:
    print(f'O número 3 aparece na posição {tupla.index(3)+1}.')
else:
    print('O número 3 não foi digitado.')

#valores pares abaixo
lista = []
for i in tupla:
    if i %2 == 0:
        np = i
        lista.append(np)
if len(lista) == 0:
    print("Não há números pares na tupla.")
else:
    print("Números pares na tupla:", lista)



