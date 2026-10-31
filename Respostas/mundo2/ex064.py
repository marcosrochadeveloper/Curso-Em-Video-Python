# Ex064 - Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número [999 para parar]: 1
# Digite um número [999 para parar]: 5
# Digite um número [999 para parar]: 10
# Digite um número [999 para parar]: 20
# Digite um número [999 para parar]: 35
# Digite um número [999 para parar]: 999
# Você digitou 5 números e a soma entre eles foi 71.
numero = countNumeros = soma = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero != 999:
        soma += numero
        countNumeros += 1
print(f'Você digitou {countNumeros} números e a soma entre eles foi {soma}.')