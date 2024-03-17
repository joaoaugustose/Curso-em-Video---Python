#questionar o nome da pessoa e verificar se possui SILVA nele.

'''n = input('Digite seu nome: ')
#'silva' in n
#sn = n.upper() == 'SILVA'
print('Seu sobrenome possuí a palavra Silva? {}'.format('silva' in n))'''

#.strip para retirar os espaços tanto antes quanto depois da frase
n = str(input('Digite seu nome completo: ')).strip()

#a formula do format, questiona se existe algum silva na palavra, jogando p caixa alta
print('Seu sobrenome possui Silva? {}'.format('SILVA' in n.upper()))

