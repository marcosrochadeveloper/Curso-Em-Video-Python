# Ex071 - Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# ==============================
#           BANCO CEV
# ==============================
# Que valor você quer sacar? R$25846
# Total de 516 cédulas de R$50.00
# Total de 2 cédulas de R$20.00
# Total de 6 cédulas de R$1.00
# ==============================
# Volte sempre ao BANCO CEV! Tenha um bom dia!

print('='*30)
print(f'{'BANCO CEV':^30}')
print('='*30)

totalCedulas50 = totalCedulas20 = totalCedulas10 = totalCedulas1 = 0

valor = float(input('Que valor você quer sacar? '))
restante = valor
if valor >= 50:
    totalCedulas50 += restante // 50
    restante -= (totalCedulas50 * 50)
if restante >= 20:
    totalCedulas20 += restante // 20
    restante -= (totalCedulas20 * 20)
if restante >= 10:
    totalCedulas10 += restante // 10
    restante -= (totalCedulas10 * 10)
totalCedulas1 = restante

if totalCedulas50 != 0 : print(f'Total de {totalCedulas50:.0f} cédulas de R$50.00')
if totalCedulas20 != 0 : print(f'Total de {totalCedulas20:.0f} cédulas de R$20.00')
if totalCedulas10 != 0 : print(f'Total de {totalCedulas10:.0f} cédulas de R$10.00')
if  totalCedulas1 != 0 : print(f'Total de {totalCedulas1:.0f} cédulas de R$1.00')

print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')