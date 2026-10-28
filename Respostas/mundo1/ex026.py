# Ex026 - Faça um programa que leia uma frase pelo teclado e mostre:
# a) Quantas vezes aparece a letra “A”.
# b) Em que posição ela aparece a primeira vez.
# c) Em que posição ela aparece a última vez.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite uma frase: Amanda ama Pedro
# A letra A aparece 5 vezes na frase
# A primeira letra A apareceu na posição 1
# A última letra A apareceu na posição 10

frase = input('Digite uma frase: ').strip()
print(f'A letra A aparece {frase.upper().count('A')} vezes na frase')
print(f'A primeira letra A apareceu na posição {frase.upper().find('A')+1}')
print(f'A última letra A apareceu na posição {frase.upper().rfind('A')+1}')