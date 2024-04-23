# lista = [[], [], []]
# listapar = list()
# soma = num = 0
#
# for i in range(0, 3):
#     num = int(input(f'Digite um número para [{0}, {i}]: '))
#     (lista[0].append(num))
#     if num % 2 == 0:
#         listapar.append(num)
# for c in range(0, 3):
#     num = int(input(f'Digite um número para [{1}, {c}]: '))
#     (lista[1].append(num))
#     if num % 2 == 0:
#         listapar.append(num)
#
# for n in range(0, 3):
#     num = int(input(f'Digite um número para [{2}, {n}]: '))
#     (lista[2].append(num))
#     if num % 2 == 0:
#         listapar.append(num)
# print('-=' * 20)
# print(lista[0])
# print(lista[1])
# print(lista[2])
# print('-=' * 20)
# soma = sum(listapar)
# print(f'A soma dos números pares é {soma}')
# soma2 = (lista[0][2] + lista[1][2] + lista[2][2])
# print(f'A soma da terceira coluna é: {soma2}')
# print(f'O maior número digitado na segunda coluna é {max(lista[1])}')

###PROFESSOR
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacoluna = 0
#para cada linha
for l in range(0, 3):
    #para cada coluna
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somapar}')
for l in range(0, 3):
    somacoluna += matriz[l][2]
print(f'A soma dos valores na terceira coluna é {somacoluna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')