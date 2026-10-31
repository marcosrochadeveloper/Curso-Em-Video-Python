# Ex044 - Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# ============ LOJAS GUANABARA ============
# Preço das compras: R$1000
# FORMAS DE PAGAMENTO
# [ 1 ] à vista dinheiro/cheque
# [ 2 ] à vista cartão
# [ 3 ] 2x no cartão
# [ 4 ] 3x ou mais no cartão
# Qual é a opção? 3
# Sua compra será parcelada em 2x de R$500.00 SEM JUROS
# Sua compra de R$1000.00 vai custar R$1000.00 no final.

print(f'{' LOJAS GUANABARA ':=^41}')
valorCompra = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
printTotal = False

if opcao == 1:
    total = valorCompra * 0.9
    print('Sua compra foi à vista em dinheiro ou cheque e você recebeu 10% de desconto!')
    printTotal = True
elif opcao == 2:
    total = valorCompra * 0.95
    print('Sua compra foi à vista no cartão e você recebeu 5% de desconto!')
    printTotal = True
elif opcao == 3:
    total = valorCompra
    print(f'Sua compra será parcelada em 2x de R${valorCompra / 2:.2f} SEM JUROS')
    printTotal = True
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = valorCompra * 1.2
    print(f'Sua compra será parcelada em {parcelas}x de R${total/parcelas:.2f} COM JUROS.')
    printTotal = True
else:
    print('Opção inválida, tente novamente!')

if printTotal:
    print(f'Sua compra de R${valorCompra:.2f} vai custar R${total:.2f} no final!')
