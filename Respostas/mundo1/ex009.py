# Ex009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número para ver sua tabuada: 6
# -------------
# 6 x  1 = 6
# 6 x  2 =  12
# 6 x  3 =  18
# 6 x  4 =  24
# 6 x  5 =  30
# 6 x  6 =  36
# 6 x  7 =  42
# 6 x  8 =  48
# 6 x  9 =  54
# 6 x 10 =  60
# -------------

numero = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
print(f'{numero} x {1:2} = {numero * 1}')
print(f'{numero} x {2:2} = {numero * 2}')
print(f'{numero} x {3:2} = {numero * 3}')
print(f'{numero} x {4:2} = {numero * 4}')
print(f'{numero} x {5:2} = {numero * 5}')
print(f'{numero} x {6:2} = {numero * 6}')
print(f'{numero} x {7:2} = {numero * 7}')
print(f'{numero} x {8:2} = {numero * 8}')
print(f'{numero} x {9:2} = {numero * 9}')
print(f'{numero} x {10:2} = {numero * 10}')
print('-'*12)
