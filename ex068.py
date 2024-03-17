from random import randint

print('-='*12)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*12)
soma = vit = 0
comp = randint(0,11)

while True:
    n = int(input('Digite um valor: '))
    s = str(input('Par ou Impar? [P/I] ')).upper()
    soma = n + comp
    print('Você colocou {} e o computador {}, deu um total de {}'.format(n, comp, soma))
    if s == 'P':
        if soma % 2 == 0:
            print('Deu PAR, você ganhou!')
            vit += 1
        else:
            print('Você perdeu!')
            break
    elif s == 'I':
        if soma % 2 == 1:
            print('Deu Impar, você ganhou!')
            vit += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente..'.format(vit))
print('GAMEOVER, Você ganhou {} vezes.'.format(vit))
