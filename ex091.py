from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)
        }
#para demonstrar o ranking, criamos a lista ranking
ranking = list()

#para cada jogador(chave) e cada número(randint) no jogo.items(que pega todas as informações)
for c, v in jogo.items():
    print(f'O {c} jogou o dado e tirou {v}')
    sleep(1)
#para o ranking usa o sorted para colocar em ordem tudo que ta na posição 1(key) e reverse true para ficar na ordem dos maiores pros menores.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('RANKING DOS VENCEDORES')
# para cara indice, o valor (como é uma lista utiliza in enumerate) rankig
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}')
    sleep(1)
