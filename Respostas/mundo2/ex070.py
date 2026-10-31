# Ex070 - Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# -----------------------------------
#       LOJA SUPER BARATÃO
# -----------------------------------
# Nome do Produto: Tesoura
# Preço: R$10
#
# Quer continuar? [S/N] s
#
# Nome do Produto: Computador
# Preço: R$1500
#
# Quer continuar? [S/N] n
#
# ----------- FIM DO PROGRAMA ------------
# O total da compra foi R$1510.00
# Temos 1 produtos custando mais de R$1000.00
# O produto mais barato foi Tesoura que custa R$10.00

print('-' * 30)
print(f'{'LOJA SUPER BARATÃO':^30}')
print('-' * 30)
total = totalDeProdutosMais1000 = contador = 0
while True:
    nomeProduto = str(input('Nome do Produto: '))
    precoProduto = float(input('Preço: R$'))
    contador += 1
    total += precoProduto

    if contador == 1 or precoProduto < precoMaisBarato:
        produtoMaisBarato = nomeProduto
        precoMaisBarato = precoProduto

    if precoProduto > 1000:
        totalDeProdutosMais1000 += 1

    continuar = ' '
    if continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar not in 'SN':
            print('RESPOSTA INVÁLIDA, TENTE NOVAMENTE!')
    if continuar == 'N':
        break

print(f'{' FIM DO PROGRAMA ':_^40}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totalDeProdutosMais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produtoMaisBarato} que custa R${precoMaisBarato:.2f}')
