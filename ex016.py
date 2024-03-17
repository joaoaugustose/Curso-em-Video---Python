### Disponibilizar um número quebrado e informar ele inteiro

#forma de fazer com parametro somente import;
'''import math
n = float(input('Digite um valor quebrado: '))
int = math.trunc(n)
print('O valor digitado foi {}, e sua porção inteira é {}'.format(n, int))'''
#forma de fazer com o parametro from import;
'''from math import trunc
n = float(input('Digite um valor quebrado: '))
print('O valor digitado foi {}, e seu valor inteiro é {}'.format(n, trunc(n)))'''
#forma de fazer sem parametros de import, somente incluindo o int como parametro nas chaves;
'''n = float(input('Digite um valor quebrado: '))
print('O valor digitado foi {}, e seu valor inteiro é {}.'.format(n, int(n)))'''
