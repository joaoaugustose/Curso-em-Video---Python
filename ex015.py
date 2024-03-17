d = int(input('Quantos dias você irá ficar com o carro? '))
k = float(input('Qual a km que você irá rodar com o carro? '))
#diaria = d * 60
#km = k * 0.15
#total = diaria + km
#print('O valor por ficar {} dias com o carro é R${:.2f}, para rodar {}km é R${:.2f}, sendo assim o total é de R${:.2f}'.format(d, diaria, k, km, total))
total = (d * 60) + (k * 0.15)
print('O valor total é de R${:.2f}'.format(total))
