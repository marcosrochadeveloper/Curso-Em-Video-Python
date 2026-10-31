# Ex045 - Crie um programa que faça o computador jogar Jokenpô com você.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# [ 0 ] PEDRA
# [ 1 ] PAPEL
# [ 2 ] TESOURA
# Qual é a sua jogada? 1
# JO
# KEN
# PO!!!
# -=-=-=-=-=-=-=-=-=-=-=
# Computador jogou PAPEL
# Jogador jogou PAPEL
# -=-=-=-=-=-=-=-=-=-=-=
# EMPATE!!!
from random import randint
from time import sleep

computador = randint(0, 2)
print("""[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA""")
jogador = int(input('Qual é a sua jogada? '))
if jogador < 0 or jogador > 2:
    print('Jogada Inválida, tente novamente!')
else:
    if jogador == 0: j = 'PEDRA'
    elif jogador == 1: j = 'PAPEL'
    elif jogador == 2: j = 'TESOURA'

    if computador == 0: c = 'PEDRA'
    elif computador == 1: c = 'PAPEL'
    elif computador == 2: c = 'TESOURA'

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-='*11)
    print(f'Computador jogou {c}')
    print(f'Jogador jogou {j}')
    print('-='*11)

    if j == c:
        print('EMPATE')
    elif (j == 'PEDRA' and c == 'PAPEL') or (j == 'PAPEL' and c == 'TESOURA') or (j == 'TESOURA' and c == 'PEDRA'):
        print('Computador Ganhou!')
    else:
        print('Jogador Ganhou!')