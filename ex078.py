lista = []

for i in range(0,5):
    lista.append(int(input(f'Digite um número, para a posição {i}: ')))
print('-='*25)
print(f'Os números digitados são: {lista}')

for p, v in enumerate(lista):
    posmaior = lista.index(max(lista))
    posmenor = lista.index(min(lista))

print(f'O menor número digitado foi o {min(lista)} na posição {posmenor}')
print(f'O maior número digitado foi o {max(lista)} na posição {posmaior}')

