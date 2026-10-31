# Ex063 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# ------------------------------
# Sequência de Fibonacci
# ------------------------------
# Quantos termos você quer mostrar? 15
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 0 → 1 → 1 → 2 → 3 → 5 → 8 → 13 → 21 → 34 → 55 → 89 → 144 → 233 → 377 → FIM
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
termos = int(input('Quantos termos você quer mostrar? '))
anterior = 0
atual = 0
proximo = 1
contador = 0
while contador < termos:
    print(f'{atual} → ', end='')
    anterior = atual
    atual = proximo
    proximo = anterior + atual
    contador += 1
print('FIM')