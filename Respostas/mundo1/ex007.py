# Ex007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeira nota do aluno: 5.5
# Segunda nota do aluno: 2
# A média entre 5.5 e 2.0 é igual a 3.8

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2

print(f'A média entre {n1} e {n2} é igual a {media:.1f}')