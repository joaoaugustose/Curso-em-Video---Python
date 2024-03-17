import random
from time import sleep
print('-='*18)
print('Vamos jogar pedra, papel e tesoura!')
print('=-'*18)
print('''Escolha uma opção:
[0] Pedra
[1] Papel
[2] Tesoura''')
opcao = int(input('Qual é a sua opção? '))

opcoes = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
sleep(1)

print('Você escolheu {}'.format(opcoes[opcao]))
print('O computador escolheu {}'.format(opcoes[computador]))

if opcao == 0 and computador == 0 or opcao == 1 and computador == 1 or opcao == 2 and computador == 2:
    print('Deu empate!')
elif opcao == 0 and computador == 1 or opcao == 1 and computador == 2 or opcao == 2 and computador == 0:
    print('Você perdeu!')
elif opcao == 0 and computador == 2 or opcao == 2 and computador == 1 or opcao == 1 and computador == 0:
    print('Você ganhou!')
else:
    print('Tente novamente.')