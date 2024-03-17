print('Vamos fazer uma tabuada!')

while True:
    tab = int(input('Digite um número e veja sua tabuada: '))
    if tab >= 0:
        for i in range (1, 11):
            print('{} x {} = {}'.format(tab, i, (tab*(i))))
    else:
        break
print('Fim do programa!')