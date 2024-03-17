## O professor quer sortear entre 4 alunos, a ordem de apresentação do trabalho.
## Fazer um programa que leia e mostre a ordem

import random
a1 = input('Digite um nome: ')
a2 = input('Digite outro nome: ')
a3 = input('Digite mais um nome: ')
a4 = input('Digite só mais um nome: ')
a5 = input('Digite só mais um nome: ')
sorteio = random.sample([a1, a2, a3, a4, a5], k=2)
print('A ordem selecionada para apresentar o trabalho será: {}'.format(sorteio))

'''import random
a1 = input('Digite um nome: ')
a2 = input('Digite outro nome: ')
a3 = input('Digite mais um nome: ')
a4 = input('Digite só mais um nome: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem selecionada para apresentar o trabalho será: {}'.format(lista))'''
