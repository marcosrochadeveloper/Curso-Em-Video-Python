# Ex056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a) A média de idade do grupo
# b) Qual é o nome do homem mais velho
# c) Quantas mulheres têm menos de 20 anos.
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# ----- 1ª Pessoa -----
# Nome: João
# Idade: 35
# Sexo [M/F]: m
# ----- 2ª Pessoa -----
# Nome: Pedro
# Idade: 20
# Sexo [M/F]: m
# ----- 3ª Pessoa -----
# Nome: Joana
# Idade: 18
# Sexo [M/F]: f
# ----- 4ª Pessoa -----
# Nome: Bianca
# Idade: 20
# Sexo [M/F]: f
# a) A média de idade do grupo é de 23.25 anos
# b) O homem mais velho tem 35 anos e se chama João
# c) No total são 1 mulheres com menos de 20 anos
somaIdades = 0
maiorIdadeHomem = 0
totalMulheres20 = 0

for c in range(1, 5):
    print(f'{f' {c}ª Pessoa ':-^21}')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: ' ))
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    somaIdades += idade
    if sexo == 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemMaiorIdade = nome
    elif sexo == 'F' and idade < 20:
        totalMulheres20 += 1

mediaIdades = somaIdades / 4

print(f'a) A média de idade do grupo é de {mediaIdades:.1f} anos')
print(f'b) O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeHomemMaiorIdade}')
print(f'c) No total são {totalMulheres20} mulheres com menos de 20 anos')
