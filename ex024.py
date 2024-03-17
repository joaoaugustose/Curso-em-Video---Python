#verificar se possui a palavra SANTO no começo da frase escrita
n = input('Em qual cidade você nasceu? ')

#dessa forma até funciona, mas quebra se a pessoa colocar letras maiusculas ou minusculas
#print('santo' in n)

#a função :5 verifica os primeiros 5 dígitos, .upper() == 'SANTO' para jogar tudo que foi escrito para maiusculo e disponibilizar se possui ou nao
print(n[:5].upper() == 'SANTO')