# Ex019 - Um professor quer sortear um de seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeiro aluno: João
# Segundo aluno: Maria
# Terceiro aluno: Josefa
# Quarto aluno: Pedro
# O aluno escolhido foi Josefa
from random import choice

alunos = []
alunos.append(input('Primeiro aluno: '))
alunos.append(input('Segundo aluno: '))
alunos.append(input('Terceiro aluno: '))
alunos.append(input('Quarto aluno: '))

print(f'O aluno escolhido foi {choice(alunos)}')