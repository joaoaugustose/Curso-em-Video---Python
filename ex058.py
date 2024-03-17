from random import randint
computador = randint(0,10)

print('Sou seu computador, adivinhe o número o qual pensei entre 0 - 10')
acertou = False
tentativa = 0
while not acertou:
    num = int(input('Digite um numero: '))
    tentativa = tentativa + 1
    if num == computador:
        acertou = True
        print('Depois de {} tentativas, você acertou!'.format(tentativa))
    else:
        print('Tente novamente!')