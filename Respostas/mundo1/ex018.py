# Ex018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite o ângulo que você deseja: 90
# O ângulo de 90.0 tem o SENO de 1.00
# O ângulo de 90.0 tem o COSSENO de 0.00
# O ângulo de 90.0 tem a TANGENTE de 16331239353195370.00
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
radiano = radians(angulo)
print(f'O ângulo de {angulo} tem o SENO de {sin(radiano):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cos(radiano):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tan(radiano):.2f}')