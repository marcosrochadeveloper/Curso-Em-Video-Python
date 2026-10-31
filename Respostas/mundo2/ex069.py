# Ex069 - Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# ------------------------------
#      CADASTRE UMA PESSOA
# ------------------------------
# Idade: 15
# Sexo: [M/F] m
# ------------------------------
# Quer continuar? [S/N] s
# ------------------------------
#      CADASTRE UMA PESSOA
# ------------------------------
# Idade: 10
# Sexo: [M/F] f
# ------------------------------
# Quer continuar? [S/N] s
# ------------------------------
#      CADASTRE UMA PESSOA
# ------------------------------
# Idade: 25
# Sexo: [M/F] m
# ------------------------------
# Quer continuar? [S/N] n
# Tivemos um total de 1 pessoas cadastradas com mais de 18 anos
# No total temos 2 homens cadastrados
# E temos 1 mulheres com menos de 20 anos
mais18 = homens = mulheresMenos20 = 0
def l(marcador):
    print(marcador * 30)

while True:
    l('~')
    print(f'{'CADASTRE UMA PESSOA':^30}')
    l('~')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
        if sexo not in 'MF':
            print('SEXO INVÁLIDO! Tente novamente!')
    if idade >= 18:
        mais18 += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1

    continuar = ' '
    while continuar not in 'SN':
        l('-')
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        l('-')
        if continuar not in 'SN':
            print('RESPOSTA INVÁLIDA! Tente novamente!')
    if continuar == 'N':
        break

print(f'Tivemos um total de {mais18} pessoas cadastradas com mais de 18 anos')
print(f'No total temos {homens} homens cadastrados')
print(f'E temos {mulheresMenos20} mulheres com menos de 20 anos')