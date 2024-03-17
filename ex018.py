### Fazer um programa que leia o angulo, e disponibilize o seno, cosseno e tangente.

import math
ang = float(input('Digite um angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno é {:.2f}.'.format(sen))
print('O cosseno é {:.2f}.'.format(cos))
print('A tangente é {:.2f}.'.format(tan))
