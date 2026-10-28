# Ex023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Informe um número: 9876
# Analisando o número 9876
# Unidade: 6
# Dezena: 7
# Centena: 8
# Milhar: 9

numero = int(input('Informe um número: '))
print(f'Analisando o número {numero}')

print(f'Unidade: {numero % 10}')
print(f'Dezena: {(numero // 10)%10}')
print(f'Centena: {(numero // 100)%10}')
print(f'Milhar: {(numero // 1000)%10}')
