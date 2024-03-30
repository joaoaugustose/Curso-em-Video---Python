# lista = []
# resposta = 'S'
# num = 0
#
# while resposta != 'N':
#     num = int(input('Digite um número: '))
#     lista.append(num)
#     resposta = str(input('Deseja continuar? [S/N]: ')).upper()
#
# print(f'Você digitou {len(lista)} elementos.')
# lista.sort(reverse=True)
# print(f'Os valores em ordem decrescente são {lista}')
# if 5 in lista:
#     print(f'O número 5 consta na sua lista.')
# else:
#     print(f'O número 5 não consta na sua lista.')

#professor

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'nN':
        break
print(f'Você digitou {len(lista)} números.')
lista.sort()
print(f'Você digitou os valores em ordem crescente: {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')