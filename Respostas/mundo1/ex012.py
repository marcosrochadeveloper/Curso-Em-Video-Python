# Ex012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Qual é o preço do produto? R$1000
# O produto que custava R$1000.00, na promoção com desconto de 5% vai custar R$950.00

produto = float(input('Qual é o preço do produto? R$'))
precoComDesconto = produto - produto * 0.05
print(f'O produto que custava R${produto:.2f}, na promoção com desconto de 5% vai custar R${precoComDesconto:.2f}')
