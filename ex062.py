print('Progressão Aritmetica')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} > '.format(termo), end='')
        termo = termo + razao
        contador = contador + 1
    print('caboci')
    mais = int(input('Quantos termos você deseja ver mais? '))
print('Foram demonstrados {} termos.'.format(total))

