#questionar o ano de nascimento

#informar se de acordo com a idade, ele ainda irá se alistar OU está no ano do alistamento OU se ja passou da hora de se alistar
from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano


print('Você nasceu em {} e tem {} anos em {}.'.format(ano, idade, date.today().year))
if idade == 18:
    print('Este é o seu ano de alistamento!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos pro seu alistamento.'.format(saldo))
elif idade > 18:
    saldo2 = idade - 18
    ano2 = date.today().year - saldo2
    print('Já passaram {} anos para seu alistamento, que seria a {} anos atrás.'.format(saldo2, ano2))
