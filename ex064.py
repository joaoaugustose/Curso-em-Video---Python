n = int(input('Digite o número 999 para parar: '))
cont = 0
while n != 999:
    soma = n + n
    cont = cont + 1
    n = int(input('Digite o número 999 para parar: '))
print('Foram digitados {} números e a soma entre eles é {}.'.format(cont, soma))
