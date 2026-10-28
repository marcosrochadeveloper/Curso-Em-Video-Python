# Ex016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um valor: 1000
# O valor digitado foi 1000.0 e a sua porção inteira é 1000
from math import trunc
valor = float(input('Digite um valor: '))
print(f'O valor digitado foi {valor} e sua porção inteira é {trunc(valor)}')
# print(f'O valor digitado foi {valor} e sua porção inteira é {int(valor)}')
