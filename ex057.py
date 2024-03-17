'''sexo = str(input('Digite o seu sexo [M/F]: ')).upper()
#se sexo diferente de M e sexo diferente de F, ler a mensagem abaixo:
while (sexo != "M" and sexo != "F"):
    sexo = str(input('Código incorreto, digite novamente: ')).upper()

print('Você digitou {}, salvamos em nossa base.'.format(sexo))'''

#professor abaixo:

#.strip para retirar espaços indesejados, .upper para identificar letras sempre maiusculas, [0] para pegar a primeira letra caso escreva masculino ou feminino
sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

#quando sexo não for M m F f, escrever a mensagem, se for, acaba o while.
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite seu sexo [M/F]: ')).strip().upper()[0]

print('Sexo {} registrado em nossa base.'.format(sexo))
