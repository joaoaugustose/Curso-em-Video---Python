si = 0
mi = 0
cont = 0
mv = 0
nmv = 0

for i in range(1, 5):
    print('---- {} PESSOA ----'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    si = si + idade
    mi = si / i
#se homem, informar o mais velho, nome e idade do mesmo.
    if sexo in ['M']:
        if idade > mv:
            mv = idade
            nmv = nome

    if sexo in ['F'] and idade < 20:
        cont = cont + 1

print('O homem mais velho possuí {} anos e se chama {}.'.format(mv, nmv))
print('A média de idade do grupo é de {} anos'.format(mi))
print('Neste grupo possuímos {} mulheres, abaixo de 20 anos.'.format(cont))
