# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo not in 'MmFf':
    sexo = input('Digite o seu sexo [M/F]: ').strip()
    if sexo not in 'MmFf':
        print('Entrada inválida. Por favor, digite M ou F.')
print(f'Sexo {sexo.upper()} registrado com sucesso.')

#IF YOU WANT IT IN ENGLISH, just remove the #

#--------------------------------------------------------------------------------------------------------------------

# Create a program that reads a person's gender but only accepts the values 'M' or 'F'.
# If the input is incorrect, ask for the input again until a valid value is provided.

# gender = ''
# while gender not in 'MmFf':
#     gender = input('Enter your gender [M/F]: ').strip()
#     if gender not in 'MmFf':
#         print('Invalid input. Please enter M or F.')
# print(f'Gender {gender.upper()} successfully registered.')