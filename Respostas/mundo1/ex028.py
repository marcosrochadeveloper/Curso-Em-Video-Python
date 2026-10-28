# Ex028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:

# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
# Vou pensar em um número entre 0 e 5. Tente adivinhar...
# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
# Em que número eu pensei? 3
# PROCESSANDO...
# GANHEI! Eu pensei no número 1 e não no 3!

# -------------------------------------------------------------

# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
# Vou pensar em um número entre 0 e 5. Tente adivinhar...
# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
# Em que número eu pensei? 0
# PROCESSANDO...
# PARABÉNS! Você conseguiu me vencer!
from random import randint
from time import sleep
print(f'\033[33m{'-=-'*20}')
print('\033[34mVou pensar em um número entre 0 e 5. Tende adivinhar...')
print(f'\033[33m{'-=-'*20}\033[m')
computador = randint(0, 5)
jogador = int(input("Em que número eu pensei? "))
print('PROCESSANDO...')
sleep(1)
if computador == jogador:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!')
else:
    print(f'\033[31mGANHEI! Eu pensei no número {computador} e não no {jogador}!')