#tirar a media de duas notas e
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
resultado = (n1+n2) / 2

#acima de 7 aprovado
if resultado >= 7:
    print('Tirando as notas {} e {}, a média fica {:.2f}, você está aprovado!'.format(n1, n2, resultado))
elif resultado < 5:
    print('Tirando as notas {} e {}, a média fica {:.2f}, você está reprovado!'.format(n1, n2, resultado))
else:
    print('Tirando as notas {} e {}, a média fica {:.2f}, você está de recuperação, boa sorte!'.format(n1, n2, resultado))
