# Ex035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#         Analisador de Triângulos
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Primeiro segmento: 3.5
# Segundo segmento: 2.75
# Terceiro segmento: 4
# Os segmentos acima PODEM FORMAR um triângulo!

# ------------------------------------------------------------

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#         Analisador de Triângulos
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Primeiro segmento: 2
# Segundo segmento: 4
# Terceiro segmento: 9
# Os segmentos acima NÃO PODEM FORMAR um triângulo!

print('\033[1;7;32m ',end='')
print('\033[1;7;32m-=\033[m'*20, end='')
print('\033[1;7;32m \033[m')

print('\033[0;1;7m ',end='')
print(f'\033[0;1;7m{'Analisador de Triângulos':^41}\033[m')

print('\033[1;7;32m ',end='')
print('\033[1;7;32m-=\033[m'*20, end='')
print('\033[1;7;32m \033[m')

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

podeFormar = True if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2 else False

if podeFormar:
    print('Os segmentos acima \033[1;7;32m PODEM FORMAR \033[m um triângulo!')
else:
    print('Os segmentos acima \033[1;7;31m NÃO PODEM FORMAR \033[m um triângulo!')