#realizar a contagem de quantas letras A aparecem, posição inicial e final

frase = str(input('Digite uma frase: ')).upper().strip()
#quantas vezes aparece
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
#em qual posição inicia
print('A primeira letra "A" apareceu na posição: {}'.format(frase.find('A')+1))
#em qual posição finaliza
print('A ultuma letra "A" apareceu na posição: {}'.format(frase.rfind('A')+1))