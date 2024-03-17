#digite o comprimento de 3 retas e diga se elas formam um triangulo;
print('-=-' *18)
print('Vamos validar 3 medidas e ver se fecha um triangulo!')
print('-=-' *18)
m1 = float(input('Digite uma medida: '))
m2 = float(input('Digite outra medida: '))
m3 = float(input('Digite mais uma medida: '))

if m1 < m2 + m3 and m2 < m3 + m1 and m3 < m1 + m2:
    print('As medidas formam um triangulo: ', end='')
    if m1 == m2 == m3:
        print('EQUILATERO!')
    elif m1 != m2 != m3 != m1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('As medidas não formam um triangulo!')
