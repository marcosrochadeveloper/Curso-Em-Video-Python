# Ex032 - Faça um programa que leia um ano qualquer e diga se ele é BISSEXTO.
# |||DICAS|||
# Todoo ano bissexto é Múltiplo de 4
# Se for múltiplo de 100 precisa ser também múltiplo de 400

# [Exemplo] A EXECUÇÃO DO PROGRAMA SERÁ COMO MOSTRADO ABAIXO:
# Que ano quer analisar? Coloque 0 para analisar o ano atual: 1900
# O ano 1900 não é bissexto!

# ---------------------------------------------------------------------

# Que ano quer analisar? Coloque 0 para analisar o ano atual: 2016
# O ano 2016 é bissexto!

# ----------------------------------------------------------------------

# Que ano quer analisar? Coloque 0 para analisar o ano atual: 0
# O ano 2025 não é bissexto!
from datetime import datetime, date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.now().year or date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'\033[1;32mO ano {ano} é bissexto!')
else:
    print(f'\033[1;31mO ano {ano} não é bissexto!')