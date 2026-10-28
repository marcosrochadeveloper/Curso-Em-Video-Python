# Ex029 - Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Qual é a velocidade atual do carro? 30
# Tenha um bom dia! Dirija com segurança!
# -------------------------------------------------------------
# Qual é a velocidade atual do carro? 120
# MULTADO! Você excedeu o limite permitido que é de 80Km/h
# Você deve pagar uma multa de R$280.00!
# Tenha um bom dia! Dirija com segurança!

velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!\033[m')
else:
    print('\033[32m', end="")
print('Tenha um bom dia! Dirija com segurança!')