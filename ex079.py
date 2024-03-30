# lista = []
# resposta = 'S'
# num = 0
#
# while resposta != 'N':
#     num = (int(input('Digite um número: ')))
#     if num not in lista:
#         lista.append(num)
#         print('Número adicionaro a lista')
#     else:
#         print('Este número já está na lista.')
#     resposta = str(input('Deseja incluir mais algum número? [S/N]: ')).upper()
#
# lista.sort()
# print(lista)

#professor:
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Número repetido, não vamos adicionar!')

    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores: {numeros}')
