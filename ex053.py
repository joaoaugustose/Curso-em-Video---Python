print('DIGITE UMA PALAVRA/FRASE E VEJA SE É UM PALINDROMO!')
pala = str(input('Digite uma palavra: ')).upper().replace(' ','')
pali = pala[::-1]

if pala == pali:
    print(f'A palavra digitada {pala}, de trás para frente é {pali}, desta forma é um palindromo.')
else:
    print(f'A palavra digitada {pala}, de trás para frente é {pali}, desta forma não é um palindromo.')
