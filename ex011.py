a1 = float(input('Qual a altura da parede? '))
l1 = float(input('Qual a largura da parede? '))
area = a1 * l1
#cada 2m ~ 1l de tinta
tinta = area / 2
print('Sua parede tem a area total de {:.2f}m, sendo assim, necessário de {:.2f}l de tinta'.format(area, tinta))
