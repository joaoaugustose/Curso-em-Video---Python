print('-'*30)
print('        LOJA DO GUTO')
print('-'*30)
sv = total = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    valor = float(input('Qual o valor? '))
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    total += valor
    if valor >= 1000:
        sv += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    if continuar == 'N':
        break
print('----- FIM DO PROGRAMA -----')
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {sv} produto acima de R$1000,00.')
print(f'O produto mais barato foi {barato}, no valor de R${menor}.')