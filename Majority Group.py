# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime

ano_atual = datetime.now().year
adulto = 0
menor = 0

for pess in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {pess}ª pessoa: '))
    idade = ano_atual - ano
    if idade >= 21:
        adulto += 1
    else:
        menor += 1
print(f'\nTotal de adultos: {adulto}')
print(f'Total menor de idade: {menor}')

#IF YOU WANT IT IN ENGLISH, just remove the #

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create a program that reads the birth year of seven people. In the end, show how many people have not yet reached adulthood and how many are already adults.

# from datetime import datetime

# current_year = datetime.now().year
# adults = 0
# minors = 0

# for person in range(1, 8):
#     birth_year = int(input(f'Enter the birth year of person {person}: '))
#     age = current_year - birth_year
#     if age >= 21:
#         adults += 1
#     else:
#         minors += 1
# print(f'Total adults: {adults}')
# print(f'Total minors: {minors}')
