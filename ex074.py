from random import randint

n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)

tupla = (n1, n2, n3, n4, n5)
print(f'Os valores sorteados são {tupla}')

print(f'O maior número apresentado é o ', max(tupla))
print(f'O menor número apresentado é o ',min(tupla))

#O professor fez desta forma:
# num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
# print(f'Os valores sorteados foram: ', end=' ')
# for n in num:
#     print(f'{n}', end=' ')
# print(f'\nO menor valor apresentado foi o {min(num)}')
# print(f'O maior valor apresentado foi o {max(num)}')