# ponto = '.'
# print('-' * 25)
# print('{:^25}'.format('Listagem de Preço'))
# print('-' * 25)
# tupla = (('Lapis', 1.75),
#          ('Borracha', 2),
#          ('Caderno', 15.90),
#          ('Estojo', 25),
#          ('Transferidor', 4.20),
#          ('Compasso', 9.99),
#          ('Mochila', 120.32),
#          ('Canetas', 22.30),
#          ('Livro', 34.90))
# for produto, valor in tupla:
#     print(f'{produto: <12} {ponto} R${valor: .2f}')
# print('-' * 25)

#professor abaixo:
tupla = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
print('-' * 40)
print(f'{"Listagem de Preço":^40}')
print('-' * 40)
for pos in range (0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R${tupla[pos]:>7.2f}')
print('-' * 40)
