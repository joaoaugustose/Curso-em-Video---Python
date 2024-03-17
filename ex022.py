#ler o nome completo de uma pessoa e mostrar:
nome = input('Digite seu nome completo: ')
print('Vamos analisar seu nome!')

#nome com todas as letras maiusculas
print('Seu nome com letras maiusculas: {}'.format(nome.upper()))

#nome com todas as letras minusculas
print('Seu nome com letras minusculas: {}'.format(nome.lower()))

#quantas letras tem no total (sem espaço)
print('Seu nome completo possui {} letras'.format(len(nome) - nome.count(' ')))

#quantas letras tem no primeiro nome
prim = nome.split()
print('Seu primeiro nome é {}, composto por {} letras.'.format(prim[0], len(prim[0])))
