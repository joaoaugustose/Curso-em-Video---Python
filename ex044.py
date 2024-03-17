print('='*10, 'LOJAS GUTO', '='*10)
valor = float(input('Qual o valor final das suas compras? R$'))

print('FORMAS DE PAGAMENTO')
print('[1] a vista débito/pix')
print('[2] a vista no crédito')
print('[3] em 2x no cartão')
print('[4] em 3x ou mais no cartão')
opcao = int(input('Qual a opção desejada? '))
vl1 = valor - (valor * 10/100)
vl2 = valor - (valor * 5/100)
vl3 = valor + (valor * 20/100)

if opcao == 1:
    print('Sua compra de R${:.2f}, ficará R${:.2f} no PIX.'.format(valor, vl1))
elif opcao == 2:
    print('Sua compra de R${:.2f}, ficará R${:.2f} no cartão de crédito a vista.'.format(valor, vl2))
elif opcao == 3:
    print('Infelizmente, em 2x no cartão eu não consigo te dar desconto e o valor final é de R${:.2f}.'.format(valor))
elif opcao == 4:
    parc = int(input('Em quantas vezes você deseja parcelar? '))
    vl4 = vl3 / parc
    print('Infelizmente, em {} parcelas eu preciso cobrar o juros da máquina.'.format(parc))
    print('O valor original da sua compra era R${:.2f}, com o juros, ficou R${:.2f}'.format(valor, vl3))
    print('O valor da parcela, será de R${:.2f}.'.format(vl4))
else:
    print('Opção invalida!')