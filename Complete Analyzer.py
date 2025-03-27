# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
totmulher = 0

for p in range (1, 5):
    print(f'{p}ª PESSOA')
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('[ M ] / [ F ]: '))
    soma_idade += idade
    media = soma_idade / 4
    if p == 1 and sexo in 'mM':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'mM' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher += 1
         
print(f'A média de idade: {media}')
print(f'O homem mais velho se chama {nome_velho} e tem {maior_idade_homem} anos.')
print(f'Mulheres abaixo de 20 anos: {totmulher}')

#IF YOU WANT IT IN ENGLISH, just remove the #

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Develop a program that reads the name, age, and gender of 4 people.
# At the end of the program, show: the average age of the group, the name of the oldest man, and how many women are under 20 years old.

# total_age = 0
# oldest_man_age = 0
# oldest_man_name = ''
# total_women_under_20 = 0

# for p in range(1, 5):
#     print(f'{p}ª PERSON')
#     name = str(input('NAME: '))
#     age = int(input('AGE: '))
#     gender = str(input('[ M ] / [ F ]: '))
#     total_age += age
#     average_age = total_age / 4
#     if p == 1 and gender in 'mM':
#         oldest_man_age = age
#         oldest_man_name = name
#     if gender in 'mM' and age > oldest_man_age:
#         oldest_man_age = age
#         oldest_man_name = name
#     if gender in 'Ff' and age < 20:
#         total_women_under_20 += 1
         
# print(f'The average age: {average_age}')
# print(f'The oldest man is {oldest_man_name} and he is {oldest_man_age} years old.')
# print(f'Women under 20 years old: {total_women_under_20}')