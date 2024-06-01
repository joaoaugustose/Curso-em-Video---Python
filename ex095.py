jogador = dict()
gol = list()
jogadores = list()

while True:
    jogador['nome'] = str(input('Digite o nome do Jogador: '))
    totp = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(0, totp):
        gol.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i + 1}? ')))
    jogador['gols'] = gol[:]
    jogador['totgol'] = sum(gol)
    jogadores.append(jogador.copy())
    gol.clear()
    resp = str(input('Deseja continuar: [S/N] ')).upper()[0]
    while resp not in 'SN':
        print('Erro, somente S ou N')
        resp = str(input('Deseja continuar: [S/N] ')).upper()[0]
    if resp == 'N':
        break

print('-=' * 30)
print(f'Codigo - {"Nome":^12} - {"Gols":^15} - {"Total":<6}')
for i, v in enumerate(jogadores):
    print(f'{i:>6} - {v["nome"]:^12} - {str(v["gols"]):<15} - {v["totgol"]:<6}')

while True:
    codigo = int(input('Mostrar os dados de qual jogador? (999 para parar) '))
    if codigo == 999:
        break
    if codigo >= len(jogadores):
        print(f'Não existe este jogador com o código {codigo}, tente novamente')
    else:
        print(f'Levantamento do jogador {jogadores[codigo]["nome"]}')
        for i, v in enumerate(jogadores[codigo]['gols']):
            print(f'Na {i + 1}ª partida, fez {v} gols')
print('Tchau')