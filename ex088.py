import random
from time import sleep

apostas = []
jogo = []
print('-=' *15)
print(f'{"Sorteador de Jogos":^30}')
print('-=' * 15)
num = int(input('Quantos jogos você deseja fazer? '))

for i in range(num):
    while len(jogo) < 6:
        numeros = random.randint(0 ,60)
        if numeros not in jogo:
            jogo.append(numeros)
    jogo.sort()
    apostas.append(jogo[:])
    jogo.clear()
print('-=' * 5, f'Vamos sortear {num} Jogos!', '-=' * 5)
for i, a in enumerate(apostas):
    print(f'{i+1}º jogo: {a}')
    sleep(1)
print(f'{"BOA SORTE!":^30}')