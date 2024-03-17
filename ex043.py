# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida


peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (alt * alt)

print('O seu IMC é: {:.2f}'.format(imc))

if imc <= 18.5:
    print('Você está abaixo do peso ideal!')
elif imc <= 25:
    print('Você está no seu peso ideal!')
elif imc <= 30:
    print('Você está com sobrepeso!')
elif imc <= 40:
    print('Cuidado, você está em obesidade!')
else:
    print('Você está com obesidade mórbida, procure um médico!')
