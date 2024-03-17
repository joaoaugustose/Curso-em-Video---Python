#dissecar números identificando por unidade, dezena, centena, milhar
num = int(input('Digite um número: '))
#realizando a conta por unidade:
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('Analisando o número: {}.'.format(num))
#print('A unidade é: {}.'.format(u))
#print('A dezena é: {}.'.format(d))
#print('A centena é: {}.'.format(c))
#print('A milhar é: {}.'.format(m))

#transformando o número em string e lendo campo a campo:
dis = str(num)
print('A unidade é {}, a dezena é {}, a centena é {} e a milhar é {}.'.format(dis[0], dis[1], dis[2], dis[3]))
