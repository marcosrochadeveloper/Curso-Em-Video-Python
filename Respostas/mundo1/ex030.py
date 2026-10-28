# Ex030 - Crie um programa que leia um número inteiro, e mostre na tela se ele é par ou ímpar.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número: 5
# O número 5 é ímpar

# --------------------------------------------------------------

# Digite um número: 12
# O número 12 é par

numero = int(input('Digite um número: '))
if numero%2 == 0:
    print(f'O número {numero} é \033[1;34mPAR')
else:
    print(f'O número {numero} é \033[1;35mÍMPAR')