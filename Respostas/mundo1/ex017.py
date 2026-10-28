# Ex017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Comprimento do cateto oposto: 5
# Comprimento do cateto adjacente: 6
# A hipotenusa vai medir 7.81
from math import hypot
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
#hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
