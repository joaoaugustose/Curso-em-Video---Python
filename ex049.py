tab = int(input('Digite um número para saber sua tabuada: '))

for i in range (0, 10):
    print('{} x {} = {}'.format(tab, i+1, (tab*(i+1))))

#comando professor
#for i in range (1,11): > adiciona um a mais no for, no meu, eu não adicionei mas adicionei no format;
#print('{} x {} = {}'.format(tab, i, tab*i))