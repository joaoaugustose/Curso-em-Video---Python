#ler o nome e identificar primeiro e último nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
sn = nome.split()
#identifica primeiro nome
print('Seu primeiro nome é: {}'.format(sn[0]))

#identifica último nome
#ele pega o SN, identifica quantas palavras possuí, o -1 faz informar a ultima palavra
print('Seu último nome é: {}'.format(sn[len(sn)-1]))

