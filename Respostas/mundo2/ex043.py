# Ex043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Maior ou igual a 18.5 e menor que 25: Peso ideal
# Maior ou igual a 25 e menor que 30: Sobrepeso
# Maior ou igual a 30 e menor que 40: Obesidade
# Maior ou igual a 40: Obesidade mórbida
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Qual é seu peso? (Kg) 75
# Qual é sua altura? (m) 1.71
# O IMC dessa pessoa é de 25.6
# Essa pessoa está em Sobrepeso!

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / altura ** 2

print(f'O IMC dessa pessoa é de {imc:.1f}')
print('Essa pessoa está ', end='')
if imc < 18.5:
    print('abaixo do peso!')
elif imc < 25:
    print('com o peso ideal!')
elif imc < 30:
    print('em Sobrepeso!')
elif imc < 40:
    print('obesa!')
else:
    print('em Obesidade mórbida.')