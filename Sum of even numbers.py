#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

total = 0
cont = 0
for c in range(6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        total += n
        cont += 1
print(f'\nVocê informou {cont} número/s par/es e a soma deles foi: {total}')

#IF YOU WANT IT IN ENGLISH, just remove the #

#-------------------------------------------------------------------------------------------------------------------------------------

# Develop a program that reads six integers and shows the sum of only those that are even. If the entered value is odd, disregard it.

# total = 0
# count = 0
# for c in range(6):
#     n = int(input('Enter a number: '))
#     if n % 2 == 0:
#         total += n
#         count += 1
# print(f'\nYou entered {count} even number/s and their sum is: {total}')
