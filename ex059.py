n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

opcao = 0

while opcao != 5:
    print('''[1] soma
[2] multiplicação
[3] maior número
[4] novos números
[5] sair''')
    opcao = int(input('Qual a opção desejada? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma do {} e {} é igual a {}'.format(n1, n2, soma))

    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação dos números {} e {} é igual a {}.'.format(n1, n2, multi))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('O maior número, entre os informados é o {}.'.format(maior))

    elif opcao == 4:
        print('Informe novos números abaixo:')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))

    elif opcao == 5:
        print('Saindo!')

    else:
        ('Número inválido, tente novamente.')

print('Obrigado por utilizar.')
