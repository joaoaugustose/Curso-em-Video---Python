notas = []
lista = []
media = 0
while True:
    nome = str(input('Digite o nome: '))
    lista.append(nome)
    nota1 = float(input('Digite a nota 1: '))
    lista.append(nota1)
    nota2 = float(input('Digite a nota 2: '))
    lista.append(nota2)
    notas.append(lista[:])
    lista.clear()
    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp in 'nN':
        break
print('-=' * 18)
print(f'{"Número":^8} {"Nome":^15} {"Media":^5}')
for pos, lis in enumerate(notas):
    media = (lis[1] + lis[2]) / 2
    print(f'{pos:^5}      {lis[0]:^9}     {media:^5}')
print('-=' * 18)
while True:
    aluno = int(input('Deseja ver a nota de algum aluno? (999 para cancelar) '))
    if aluno == 999:
        break
    if aluno <= len(notas) - 1:
        print(f'Notas de {notas[aluno][0]} são {notas[aluno][1]} e {notas[aluno][2]}.')
print('Saindo...')
