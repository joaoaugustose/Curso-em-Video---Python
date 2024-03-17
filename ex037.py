#conversor de base númerica, ler um número e o usuário irá escolher entre
#1 > binário
#2 > octal
#3 > hexadecimal

num = (int(input('Defina um número inteiro: ')))
print('Escolha uma das bases, para realizar a conversão: ')
print('[ 1 ] > Converter para bínario')
print('[ 2 ] > Converter para octal')
print('[ 3 ] > Converter para hexadecimal')
opcao = int(input('Qual será sua opção? '))

if opcao == 1:
    print('O número digitado é {}, e convertido para binário é {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número digitado é {}, e convertido para octal é {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número digitado é {}, e convertido para hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção não existe.')