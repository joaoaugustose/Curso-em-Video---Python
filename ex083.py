exp = str(input('Digite uma expressão matemática: '))
pilha = []
#para cada simbolo ( ou ) na expressão:
for simbolo in exp:
    #se tiver o simbolo "(" adicionar na lista
    if simbolo == '(':
        pilha.append('(')
        #se tiver o simbolo ")" remover o "(" da lista.
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        #se a pilha tiver vazia, adicionar o ")"
        else:
            pilha.append(')')
            break
#no caso, toda vez que a expressão iniciar com o (, tem que fechar com o ). caso contrário, a expressão estará incorreta.
if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta.')