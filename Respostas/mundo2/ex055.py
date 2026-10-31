# Ex055 - Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Peso da 1 pessoa: 80
# Peso da 2 pessoa: 85
# Peso da 3 pessoa: 65
# Peso da 4 pessoa: 93
# Peso da 5 pessoa: 112
# O maior peso lido foi de 112.0Kg
# O menor peso lido foi de 65.0Kg

for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    if peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso

print(f'O maior peso lido foi de {maior:.1f}Kg')
print(f'O menor peso lido foi de {menor:.1f}Kg')