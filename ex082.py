lista = []
listapar = []
listaimpar = []
resposta = 'S'
num = 0

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    resposta = str(input('Deseja continuar? [S/N] ')).upper()
    if resposta in 'Nn':
        break

print(f'A lista com todos os números digitados foram: {lista}')
print(f'A lista de pares é: {listapar}')
print(f'A lista de ímpares é: {listaimpar}')

