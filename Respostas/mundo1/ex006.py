# Ex006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo, e raiz quadrada.
#[DICA]:
# Qualquer número elevado a 0.5 resultará em sua raiz quadrada por exemplo:
# 85**0.5 vai ser igual a 9.22 || 81**0.5 vai ser igual a 9
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite um número: 85
# O dobro de 85 vale 170.
# O triplo de 85 vale 255.
# A raiz quadrada de 85 é igual a 9.22.

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero**(1/2)
print(f'O dobro de {numero} é {dobro}')
print(f'O triplo de {numero} é {triplo}')
print(f'A raiz quadrada de {numero} é {raizQuadrada:.2f}')