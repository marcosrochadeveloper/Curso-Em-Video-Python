# Ex067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Quer ver a tabuada de qual valor? 5
# ------------------------------
# 5 x  1 = 5
# 5 x  2 = 10
# 5 x  3 = 15
# 5 x  4 = 20
# 5 x  5 = 25
# 5 x  6 = 30
# 5 x  7 = 35
# 5 x  8 = 40
# 5 x  9 = 45
# 5 x 10 = 50
# ------------------------------
# Quer ver a tabuada de qual valor? -1
# ------------------------------
# PROGRAMA TABUADA ENCERRADO. Volte sempre!

while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('-='*15)
    if numero >= 0:
        for c in range(1, 11):
            print(f'{numero} x {c:>2} = {numero * c}')
        print('-=' * 15)
    else:
        break

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')