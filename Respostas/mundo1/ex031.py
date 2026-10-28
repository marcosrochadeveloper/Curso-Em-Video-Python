# Ex031 - Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Qual a distância da sua viagem? 150
# Sua viagem de 150.0Km custará R$75.00

# --------------------------------------------------------------

# Qual a distância da sua viagem? 210
# Sua viagem de 210.0Km custará R$94.50

distancia = float(input('Qual a distância da sua viagem? '))

#total = distancia * 0.5 if distancia <= 200 else distancia * 0.45
if distancia <= 200:
    total = distancia * 0.5
else:
    total = distancia * 0.45
print(f'Sua viagem de \033[1;7;32m{distancia:.1f}Km\033[m custará \033[1;7;32mR${total:.2f}\033[m')