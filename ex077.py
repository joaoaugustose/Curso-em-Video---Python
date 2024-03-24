vogal = 'AEIOU'

tupla = ('APRENDER',
         'PROGRAMAR',
         'LINGUAGEM',
         'PYTHON',
         'CURSO',
         'GRATIS',
         'ESTUDAR',
         'PRATICAR',
         'TRABALHAR',
         'MERCADO',
         'PROGRAMADOR',
         'FUTURO')

for palavra in tupla:
    print(f'\nNa palavra {palavra}, temos as vogais ', end='')
    for letra in palavra:
        if letra in vogal:
            print(f'{letra}', end=' ')
