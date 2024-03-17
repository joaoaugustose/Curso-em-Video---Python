print('='*30)
print('{:^30}'.format('GUTO"s BANK'))
print('='*30)

saque = int(input('Digite o valor que você deseja sacar: '))
tot = saque
ced = 50
totced = 0

while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Você retirou {totced} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if tot == 0:
            break

