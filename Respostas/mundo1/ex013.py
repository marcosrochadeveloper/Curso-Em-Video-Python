# Ex013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Qual é o salário do Funcionário? R$2000
# Um funcionário que ganhava R$2000.00, com 15% de aumento, passa a receber R$2300.00

salario = float(input('Qual é o salário do Funcionário? R$'))
novoSalario = salario * 1.15
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novoSalario:.2f}')