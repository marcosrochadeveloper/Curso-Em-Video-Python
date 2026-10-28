# Ex033 - Faça um programa que leia 3 números, e mostre qual é o maior e qual é o menor.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeiro valor: 7
# Segundo valor: 2
# Terceiro valor: 4
# O menor valor digitado foi 2
# O maior valor digitado foi 7

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
menor = v1
if v2 < v1 and v2 < v3 : menor = v2
if v3 < v1 and v3 < v2 : menor = v3

maior = v1
if v2 > v1 and v2 > v3 : maior = v2
if v3 > v1 and v3 > v2 : maior = v3

print(f'\033[1;7m O menor valor digitado foi {menor} \033[m')
print(f'\033[1;7;32m O maior valor digitado foi {maior} \033[m')