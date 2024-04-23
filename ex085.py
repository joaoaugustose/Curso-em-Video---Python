lista = [[], []]
num = 0

for i in range(1, 9):
    num = int(input(f'Digite o {i} número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'Os números pares que foram digitados são: {lista[0]}')
print(f'Os números impares que foram digitados são: {lista[1]}')
