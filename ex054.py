from datetime import date
soma = 0
menor = 0

for i in range(1, 8):
    ano = int(input(f'Em que ano a {i} pessoa nasceu? '))
    idade = date.today().year - ano

    if idade > 18:
        soma = soma + 1
    else:
        menor = menor + 1

print('Temos {} pessoas com mais de 18 anos'.format(soma))
print('Temos {} pessoas com menos de 18 anos'.format(menor))
