lista = []
dic = {}
smid = list()
validador = False

while True:
    dic['nome'] = str(input('Digite o nome: '))

    sexo = str(input('Digite o sexo: [M/F] ')).upper()[0]
    while sexo not in 'mMfF':
        print('Erro, somente M ou F')
        sexo = str(input('Digite o sexo: [M/F] ')).upper()[0]
    dic['sexo'] = sexo

    idade = int(input('Digite a idade: '))
    dic['idade'] = idade
    smid.append(idade)

    lista.append(dic.copy())

    resp = str(input('Deseja continuar: [S/N] ')).upper()[0]
    while resp not in 'SN':
        print('Erro, somente S ou N')
        resp = str(input('Deseja continuar: [S/N] ')).upper()[0]
    if resp == 'N':
        break

media = (sum(smid) / len(smid))

print(f'Ao todo temos {len(lista)} cadastradas.')
print(f'A média de idade é de {media} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

print('Lista das pessoas que estão acima da média de idade: ')
# for p in lista:
#     if p['idade'] >= media:
#         print(f'Nome: {p["nome"]} ; Sexo: {p["sexo"]} ; Idade: {p["idade"]} ; ')

#linhaprofessor
for p in lista:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('Acabou!')