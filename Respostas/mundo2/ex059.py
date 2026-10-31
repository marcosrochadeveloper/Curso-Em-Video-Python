# Ex059 - Crie um programa que leia dois valores e mostre um lib na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Primeiro valor: 5
# Segundo valor: 5
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Números
# [ 5 ] Sair do Programa
# >>>>> Qual é a sua opção? 2
# O resultado de 5 x 5 é 25
# =-==-==-==-==-==-==-==-==-==-=
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Números
# [ 5 ] Sair do Programa
# >>>>> Qual é a sua opção? 5
# Finalizando...
# =-==-==-==-==-==-==-==-==-==-=
from unittest import case
from time import sleep
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input("""=-==-==-==-==-==-==-==-==-==-=
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
=-==-==-==-==-==-==-==-==-==-=
Qual é a sua opção? """))
    match opcao:
        case 1:
            print(f'O resultado de {valor1} + {valor2} é {valor1 + valor2}')
        case 2:
            print(f'O resultado de {valor1} * {valor2} é {valor1 * valor2}')
        case 3:
            if valor1 != valor2:
                print(f'Entre {valor1} e {valor2} o maior valor é', end= ' ')
                if valor1 > valor2:
                    print(valor1)
                elif valor2 > valor1:
                    print(valor2)
            else:
                print('Os dois valores são iguais!')
        case 4:
            valor1 = int(input('Redigite o primeiro valor: '))
            valor2 = int(input('Redigite o segundo valor: '))
        case 5:
            print('Finalizando...')
            sleep(1)
            print('Fim do programa! Volte sempre!')
        case _:
            print('Opção Inválida! Tente Novamente')

