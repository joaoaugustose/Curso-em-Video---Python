salario = float(input('Digite o salário do funcionário: R$'))
novo = salario + (salario * 15/100)
print('O salário é de R${:.2f}, com o reajuste de 15%, ficou R${:.2f}'.format(salario, novo))
