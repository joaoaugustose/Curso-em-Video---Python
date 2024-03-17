r = 'S'
cont = 0
soma = 0
media = 0
maior = 0
menor = 0

while r != 'N':
    num = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
    soma = soma + num
    cont = cont + 1
    media = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('Você digitou {} vezes, a média entre eles é {}'.format(cont, media))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))