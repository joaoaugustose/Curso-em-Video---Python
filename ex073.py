cont = 0
campeonato = ('Amazonas', 'America MG', 'Avai', 'Botafogo', 'Brusque', 'CRB', 'Ceara', 'Chapecoense', 'Coritiba', 'Goias', 'Guarani', 'Ituano', 'Mirassol', 'Novorizontino', 'Operário', 'Paysandu', 'Ponte Preta', 'Santos', 'Sport', 'Vila Nova')
print('-='*20)
print(f'Os times que estão na série B do campeonato são: ', campeonato)
print('-='*20)
print(f'Os 4 primeiros colocados que vão para a série A são: ', campeonato[0:4])
print('-='*20)
print(f'Os 4 últimos colocados que serão rebaixados são: ', campeonato[-4:])
print('-='*20)
#utilizando a index da tupla
posicao = campeonato.index('Avai')
print(f'O Avai está na {posicao+1}ª posição.')

#utilizando for para encontrar
##for i in campeonato:
##    cont += 1
##    if i == 'Avai':
##        print(f'O Avaí está na {cont}ª posição.')