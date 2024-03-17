#calcule o preço da viagem;
#pergunte a distancia da viagem em km;
km = int(input('Qual a distancia em km, da sua viagem? '))

#cobrar 0,50/km para viagens até 200km
km1 = km * 0.50

#cobrar 0,45/km para viagens acima de 200km
km2 = km * 0.45

print('A sua viagem, será de {}km.'.format(km))
if km <= 200:
    print('O valor é de R${:.2f}'.format(km1))
else:
    print('O valor é de R${:.2f}'.format(km2))
