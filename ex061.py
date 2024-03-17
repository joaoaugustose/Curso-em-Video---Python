print('Progressão Aritmetica')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
contador = 1

while contador <= 10:
    print('{} > '.format(termo), end=' ')
    termo = termo + razao
    contador = contador + 1

print('caboci')

