# dados = {}
#
# nome = str(input('Digite o nome do aluno: '))
# dados['nome'] = nome
# media = int(input(f'Digite a média de {dados["nome"]}: '))
# dados['media'] = media
#
# if dados['media'] >= 7:
#     print(f'{dados["nome"]} possuí uma média de {dados["media"]}, desta forma está aprovado!')
# else:
#     print(f'{dados["nome"]} possuí uma média de {dados["media"]}, desta forma está reprovado!')

#PROFESSOR
aluno = dict()
aluno['nome'] = str(input('Digite o nome: '))
aluno['media'] = float(input(f'Digite a média do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media']:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')