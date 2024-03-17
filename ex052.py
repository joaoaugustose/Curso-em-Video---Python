num = int(input('Digite um numero: '))
soma = 0

if num > 1 and num != 0:
    for i in range(2, num+1):
        if num % i == 0 and num > 1:
            soma = soma + 1
    if soma == 1:
        print('O numero {} é primo'.format(num))
    else:
        print('O numero {} não é primo'.format(num))
elif num == 1:
    print('O numero 1 não entra no quadro dos primos')
elif num == 0:
    print('Zero não é primo')
else:
    print('Numeros negativos não são primos')
