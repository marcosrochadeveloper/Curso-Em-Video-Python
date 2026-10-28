# Ex008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros, entre outras medidas de tamanhos.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Uma distância em metros: 3
# A medida de 3.0m corresponde a:
# 0.003km
# 0.03hm
# 0.3dam
# 30dm
# 300cm
# 3000mm

distancia = float(input("Uma distância em metros: "))
print(f'A medida de {distancia:.1f}m corresponde a: ')
print(f'{distancia/1000}km')
print(f'{distancia/100}hm')
print(f'{distancia/10}dam')
print(f'{distancia*10:.0f}dm')
print(f'{distancia*100:.0f}cm')
print(f'{distancia*1000:.0f}mm')