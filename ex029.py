#informar a velocidade, se ultrapassar 80km, multar e informar valor de 7 reais por km
km = int(input('Qual a velocidade do veículo? '))
multa = (km - 80) * 7

if km <= 80:
    print('Tenha um ótimo dia, dirija com segurança!')
else:
    print('Você foi multado, o limite da via é 80km/h, você passou a {}km/h!'.format(km))
    print('O valor da sua multa é de R${:.2f}'.format(multa))

