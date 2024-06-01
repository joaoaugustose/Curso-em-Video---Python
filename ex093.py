jogador = dict()
gol = list()

jogador['nome'] = str(input('Digite o nome do Jogador: '))
totp = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(0, totp):
    gol.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i+1}? ')))
jogador['gols'] = gol[:]
jogador['totgol'] = sum(gol)

print('-=' * 15)
print(jogador)

print('-=' * 15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' *15)
print(f'O jogador {jogador["nome"]} participou de {totp} partidas.')
for i, v in enumerate(gol):
    print(f'Na {i+1}ª partida, fez {v} gols')
print(f'Foi um total de {jogador["totgol"]} gols.')