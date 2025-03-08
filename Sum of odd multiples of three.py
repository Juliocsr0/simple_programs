# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('\nA soma de todos os valores solicitados é:\n')
total = 0
contagem = 0
for soma in range(1, 501, 2):
    if soma % 3 == 0:
        contagem += 1
        total += soma
print(f'Total: {total}')
print(f'Quantidade de números ímpares múltiplos de três: {contagem}')

#IF YOU WANT IT IN ENGLISH, just remove the #

#------------------------------------------------------------------------------------------------------------------------

# Create a program that calculates the sum of all numbers that are multiples of three and are in the range from 1 to 500.

# print('\nThe sum of all requested values is:\n')
# total = 0
# count = 0
# for num in range(1, 501, 2):
#     if num % 3 == 0:
#         count += 1
#         total += num
# print(f'Total: {total}')
# print(f'Number of odd multiples of three: {count}')
