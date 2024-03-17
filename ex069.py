print('-'*20)
print('Cadastre uma pessoa!')
print('-'*20)
si = ss = sf = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if idade >= 18:
        si = si + 1
    if sexo == 'M':
        ss = ss + 1
    if sexo == 'F' and idade < 20:
        sf = sf + 1
    if cont == 'N':
        break
print(f'Temos um total de {si} pessoas com mais de 18 anos.')
print(f'Ao todo, temos {ss} homem cadastrado.')
print(f'Temos {sf} mulheres com menos de 20 anos.')

##professor
