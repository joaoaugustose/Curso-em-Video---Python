import random
from time import sleep

print('Vou pensar em um número entre 0 e 5, será se você adivinha?')
n = int(input('Qual número você acha que é: '))
n1 = random.randint(0, 5)

#print('O número que pensei é o {}, e o que você digitou é {}.'.format(n1, n))

print('PROCESSANDO..')
sleep(3)

if n == n1:
    print('Você acertou, eu pensei no {} e você digitou o {}.'.format(n1, n))
else:
    print('Você errou, o número que eu pensei é o {}, e você digitou o {}.'.format(n1, n))
