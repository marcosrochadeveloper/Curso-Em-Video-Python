# Ex061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Gerador de PA
# -=-=-=-=-=-=-=-=-=-=
# Primeiro termo: 1
# Razão da PA: 5
# 1 → 6 → 11 → 16 → 21 → 26 → 31 → 36 → 41 → 46 → FIM

print('Gerador de PA')
print('-=' * 10)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiroTermo
contador = 1
while contador <= 10:
    print(f'{termo} → ', end='')
    termo += razao
    contador += 1
print('FIM')