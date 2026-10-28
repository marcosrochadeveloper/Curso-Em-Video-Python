# Ex004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite algo: Programador
# O tipo primitivo desse valor é <class 'str'>
# Só tem espaços?   False
# É um número?   False
# É alfabético?   True
# É alfanumérico?   True
# Está em maiúsculas?   False
# Está em minúsculas?   False
# Está capitalizada?   True

frase = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(frase))
print('Só tem espaços? ', frase.isspace())
print('É um número? ', frase.isnumeric())
print('É alfabético? ', frase.isalpha())
print('É alfanumérico? ', frase.isalnum())
print('Está em maiúsculas? ', frase.isupper())
print('Está em minúsculas? ', frase.islower())
print('Está capitalizada? ', frase.istitle())