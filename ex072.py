tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'O número digitado é o {tupla[num]}.')
        break
    else:
        print('Número incorreto, tente novamente. ', end='')
print('FIM')