# lista = [[], [], []]
# num = 0
#
# for i in range(0, 3):
#     num = int(input(f'Digite um número para [{0}, {i}]: '))
#     (lista[0].append(num))
#
# for c in range(0, 3):
#     num = int(input(f'Digite um número para [{1}, {c}]: '))
#     (lista[1].append(num))
#
# for n in range(0, 3):
#     num = int(input(f'Digite um número para [{2}, {n}]: '))
#     (lista[2].append(num))
#
# print(lista[0])
# print(lista[1])
# print(lista[2])

#PROFESSOR
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#para cada linha
for l in range(0, 3):
    #para cada coluna
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()