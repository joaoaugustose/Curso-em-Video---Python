#aprovar emprestimo bancário p/ compra de uma casa
print('Vamos simular o empréstimo para compra da sua casa!')

#pergunte o valor da casa
casa = int(input('Por gentileza, informe qual seria o valor da casa? R$'))

#pergunte o salário
salario = int(input('Qual seria o seu salário? '))

#pergunte em quantos anos ele vai pagar
tempo = int(input('Em quantos anos você deseja realizar o pagamento? '))
tempo2 = tempo * 12
#a prestação não pode exceder 30% do salário
prestacao = casa / tempo2

print('Você quer comprar uma casa no valor de R${:.2f}, para pagar em {} anos/{} meses e seu salário é de R${:.2f}.'.format(casa, tempo, tempo2, salario))
print('O valor da prestação é R${:.2f}'.format(prestacao))
if (salario * 0.30) >= prestacao:
    print('O emprestimo está aprovado!')
else:
    print('O emprestimo foi negado pelo seu salário não atingir 30% da prestação!')
