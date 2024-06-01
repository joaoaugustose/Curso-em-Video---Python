from datetime import date

ano = date.today().year
pessoa = dict()

pessoa['nome'] = str(input('Digite o nome: '))
pessoa['ano'] = int(input('Digite o ano de nascimento: '))

pessoa['ctps'] = int(input('Digite o número da carteira de trabalho: [0 para inexistente] '))
if pessoa['ctps'] == 0:
    print('-=' * 15)
    print(f'O nome é: {pessoa["nome"]}')
    print(f'{pessoa["nome"]} nasceu no ano de {pessoa["ano"]}')
    print(f'{pessoa["nome"]} ainda não possuí uma carteira de trabalho.')
    # for i, v in pessoa.items():
    #     print(f'{i} tem o valor de {v}')
else:
    pessoa['idade'] = (ano - pessoa['ano'])
    pessoa['contratado'] = int(input('Qual o ano de contratação: '))
    pessoa['salario'] = int(input('Qual o valor do salário: R$'))
    pessoa['aposenta'] = (pessoa['contratado'] + 35)
    pessoa['idap'] = (pessoa['aposenta'] - pessoa['ano'])

    print('-=' * 15)
    print(f'O Nome é {pessoa["nome"]}')
    print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos de idade')
    print(f'Possui a carteira de trabalho de registro {pessoa["ctps"]}')
    print(f'A contratação foi no ano de {pessoa["contratado"]}')
    print(f'Possuí o salário no valor de R${pessoa["salario"]:.2f}')
    print(f'Irá se aposentar com {pessoa["idap"]} anos de idade')