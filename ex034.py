import math
#identifica o salario
salario = float(input('Informe seu salário: R$'))
ns1 = salario + (salario * 10/100)
ns2 = salario + (salario * 15/100)

#para salarios acima de 1250, aumento de 10%
#salarios abaixo 15%

if salario >= 1250:
    print('O seu salário é de R${:.2f}, e passará a ser {:.2f}.'.format(salario, ns1))
else:
    print('O seu salário é de R${:.2f}, e passará a ser de R${:.2f}.'.format(salario, ns2))
