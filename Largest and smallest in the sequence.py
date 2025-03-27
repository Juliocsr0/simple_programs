# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}ª PESSOA: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso encontrado foi: {maior}')
print(f'O menor peso encontrato foi: {menor}')


#IF YOU WANT IT IN ENGLISH, just remove the #

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Create a program that reads the weight of five people. At the end, show which was the highest and lowest weight recorded.

# highest = 0
# lowest = 0

# for person in range(1, 6):
#     weight = float(input(f'Enter the weight of person {person}: '))
#     if person == 1:
#         highest = weight
#         lowest = weight
#     else:
#         if weight > highest:
#             highest = weight
#         if weight < lowest:
#             lowest = weight
# print(f'Highest weight: {highest}')
# print(f'Lowest weight: {lowest}')