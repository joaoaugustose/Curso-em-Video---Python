valor = float(input('Qual o valor do produto? R$'))
desc = valor - (valor*5/100)
print('o valor do produto é R${:.2f}, com desconto de 5%, ficou R${:.2f}.'.format(valor, desc))