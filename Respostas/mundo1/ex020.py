# Ex020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeiro aluno: Pedro
# Segundo aluno: Pablo
# Terceiro aluno: Petrus
# Quarto aluno: Pietro
# A ordem de apresentação será:
# ['Petrus', 'Pablo', 'Pietro', 'Pedro']

from random import shuffle

alunos = []
alunos.append(input('Primeiro aluno: '))
alunos.append(input('Segundo aluno: '))
alunos.append(input('Terceiro aluno: '))
alunos.append(input('Quarto aluno: '))

shuffle(alunos)

print(" A ordem de apresentação será:")
print(alunos)