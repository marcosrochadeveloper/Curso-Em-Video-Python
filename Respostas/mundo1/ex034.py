# Ex034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Qual é o salário do funcionário? R$900
# Quem ganhava R$900.00 passa a ganhar R$1035.00 agora.
# Qual é o salário do funcionário? R$9000
# Quem ganhava R$9000.00 passa a ganhar R$9900.00 agora.

salario = float(input('Qual é o salário do funcionário? '))

if salario > 1250:
    novosalario = salario * 1.1
else:
    novosalario = salario * 1.15

print(f'Quem ganhava \033[1;7;31m R${salario:.2f} \033[m passa a ganhar \033[1;7;32m R${novosalario:.2f} \033[m agora.')