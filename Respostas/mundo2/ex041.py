# Ex041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Ano de Nascimento: 2005
# O atleta tem 20 anos.
# Classificação: SÊNIOR
from datetime import date
anoNascimento = int(input('Ano de Nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
print(f'O atleta tem {idade} anos')
print('Classificação: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')