num = cont = soma = 0
while True:
    num = int(input('Digite um número (tecle 999 pra parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print('Foram digitados {} números e a soma entre eles é: {}'.format(cont, soma))

