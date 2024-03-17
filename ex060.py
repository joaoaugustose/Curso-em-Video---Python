##FATORIAL##

fatorial = int(input('Informe um número, para entregar a fatoração: '))

resultado = 1
contagem = 1

while contagem <= fatorial:
    resultado = resultado * contagem
    contagem = contagem + 1

print(resultado)
