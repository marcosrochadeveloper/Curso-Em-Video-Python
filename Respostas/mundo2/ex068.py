# Ex068 - Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# VAMOS JOGAR PAR OU ÍMPAR
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Diga um valor (0 à 10): 5
# Par ou Ímpar? [P/I] p
# ------------------------------
# Você jogou 5 e o computador 1. Total de 6 DEU PAR
# ------------------------------
# Você VENCEU!
# Vamos jogar novamente...
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Diga um valor (0 à 10): 2
# Par ou Ímpar? [P/I] i
# ------------------------------
# Você jogou 2 e o computador 6. Total de 8 DEU PAR
# ------------------------------
# Você PERDEU!
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# GAME OVER! Você venceu 1 vezes.
from random import randint

print('=-'*15)
print(f'{'VAMOS JOGAR PAR OU ÍMPAR':^30}')
print('=-'*15)
totalVitorias = 0

while True:
    valor = int(input('Diga um valor (0 à 10): '))
    valorComputador = randint(0, 10)
    jogada = input('Par ou Ímpar? [P/I] ').strip().upper()[0]

    total = valor + valorComputador

    print('-' * 30)
    print(f'Você jogou {valor} e o computador {valorComputador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)

    if (jogada == 'P' and total % 2 == 0) or (jogada == 'I' and total % 2 != 0):
        print('Você VENCEU!\nVamos jogar novamente...')
        totalVitorias += 1
    else:
        break

print('Você PERDEU!')
print('=-' * 15)
print(f'GAME OVER! Você venceu {totalVitorias} vezes.')
print('-=' * 15)
