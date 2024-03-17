#definir a hipotenusa, disponibilizando o cateto oposto e adjacente.

#sempre que utilizar dois digitos no import, usar como exemplo (ca, co)
#para calcular a hipotenusa possuí um "import" específico que já faz a conta automaticamente

'''import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = math.hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hip))'''

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hi))

#sem o metodo import
'''co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A medida da hipotenusa é: {:.2f}'.format(hi))'''
