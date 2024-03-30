lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
#se for o primeiro número OU se o número for o maior número da lista:
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        #enquanto a posição for menor que a leitura de lista:
        posicao = 0
        while posicao < len(lista):
            #verifica se o número que está sendo inserido é menor ou igual a lista na posição
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao += 1
print('-=' * 30)
print(f'Os valores digitados na lista em ordem é {lista}')