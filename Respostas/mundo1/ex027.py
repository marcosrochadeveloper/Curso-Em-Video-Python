# Ex027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite seu nome completo: Pedro da Silva Moreira
# Muito prazer em te conhecer Pedro!
# Seu primeiro nome é Pedro
# Seu último nome é Moreira

nome = input('Digite seu nome completo: ').strip()
nome_dividido = nome.split()
print(f'Muito prazer em te conhecer {nome_dividido[0]}!')
print(f'Seu primeiro nome é {nome_dividido[0]}')
print(f'Seu último nome é {nome_dividido[-1]}')
