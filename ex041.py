from datetime import date
ano = int(input('Digite o seu ano de nascimento, que vamos separar por categoria conforme a idade: '))
atual = date.today().year
idade = atual - ano
print('O atleta possuí {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM')
#elif idade >= 9 and idade < 14:
elif idade <= 14:
    print('Categoria: JUNIOR')
#elif idade >= 14 and idade < 19:
elif idade <= 19:
    print('Categoria: INFANTIL')
#elif idade >=19 and idade < 25:
elif idade <= 25:
    print('Categoria: SENIOR')
else:
    (print('Categoria: MASTER'))
