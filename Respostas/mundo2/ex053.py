# Ex053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Digite uma frase: apos a sopa
# O inverso de APOSASOPA é APOSASOPA
# Temos um palíndromo!

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
tudoJunto = ''.join(palavras)
fraseAoContrario = tudoJunto[::-1]
# inverso = []
# for c in range(len(tudoJunto)-1, -1, -1):
#     inverso.append(tudoJunto[c])
# fraseAoContrario = ''.join(inverso)

print(f'O inverso de {tudoJunto} é {fraseAoContrario}')
if tudoJunto == fraseAoContrario:
    print('Temos um palíndromo!')
else:
    print('E não é um palíndromo!')
