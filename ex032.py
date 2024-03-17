from datetime import date
#ler o ano e informar se o mesmo é bisexto;
ano = int(input('Informe um ano para informar se é bissexto ou não. Coloque 0 para ano atual: '))

#identifica o ano em que estamos
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bisexto.'.format(ano))
else:
    print('O ano {} não é bisexto.'.format(ano))
