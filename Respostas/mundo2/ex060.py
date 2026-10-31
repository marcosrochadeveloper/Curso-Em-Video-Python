# Ex060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número para calcular seu fatorial: 5
# Calculando 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite um número para calcular seu fatorial: '))
c = numero
totalFatorial = 1
print(f'Calculando {numero}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if numero > 1 else ' = ', end='')
    totalFatorial *= c
    c -= 1
print(f'{totalFatorial}')