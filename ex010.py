real = float(input('Quantos reais você possuí na carteira? R$'))
dolar = (real/4.91)
print('Com R${:.2f}, você consegue comprar US${:.2f}.'.format(real, dolar))
