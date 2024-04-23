pessoal = list()
dados = list()
totpes = maior = menor = 0

while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    if len(pessoal) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoal.append(dados[:])
    dados.clear()
    totpes += 1

    resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn':
        break

print(pessoal)
print(f'Ao todo, você cadastrou {totpes} pessoas.')

print(f'O maior peso cadastrado foi de {maior}kg. Peso de ', end='')
for p in pessoal:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso cadastrado foi de {menor}kg. Peso de ', end='')
for p in pessoal:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
