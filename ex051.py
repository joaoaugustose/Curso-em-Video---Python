'''print('-='*20)
print('10 termos de uma progressão aritmetica!')
print('-='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(0, 10):
    print(termo, end=' -> ')
    termo = termo + razao
print('Acabou!')'''

#CÓDIGO PROFESSOR
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for i in range(primeiro, decimo + razao, razao):
    print('{}'.format(i), end=' -> ')
print('Acabou!')
