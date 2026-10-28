# Ex022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas e minúsculas.
# b) Quantas letras ao todo (sem considerar espaços).
# c) Quantas letras tem o primeiro nome.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite seu nome completo: José Antônio Pereira Albuquerque
# Analisando seu nome...
# Seu nome em maiúsculas é JOSÉ ANTÔNIO PEREIRA ALBUQUERQUE
# Seu nome em minúsculas é josé antônio pereira albuquerque
# Seu nome tem ao todo 29 letras
# Seu primeiro nome é José e ele tem 4 letras

nome = str(input('Digite seu nome completo: ')).strip()
nomeDividido = nome.split()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len("".join(nomeDividido))} letras')
print(f'Seu primeiro nome é {nomeDividido[0]} e ele tem {len(nomeDividido[0])} letras')