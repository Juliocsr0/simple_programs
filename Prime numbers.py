# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# n = int(input('Digite um numero inteiro: '))
# if n > 1:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print(f'O número {n} NÃO é PRIMO!')
#             break
#     else:
#         print(f'O número {n} é PRIMO!')

n = int(input('Digite um numero inteiro: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')
        total += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {n} foi dividido {total} vezes!')

if total == 2:
    print('E por isso ele é um número PRIMO!')
else:
    print('E por isso ele não é um número PRIMO!')
    
#IF YOU WANT IT IN ENGLISH, just remove the #

#-----------------------------------------------------------------------------------------------------------------
    
# Create a program that reads an integer and says whether it is a prime number or not.

# n = int(input('Enter an integer: '))
# if n > 1:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print(f'The number {n} is NOT PRIME!')
#             break
#     else:
#         print(f'The number {n} is PRIME!')

#----------------------------------------------------------------------------------------------
# (i prefer this way).

# n = int(input('Enter an integer: '))
# total = 0
# for c in range(1, n + 1):
#     if n % c == 0:
#         print(f'\033[32m{c}\033[m', end=' ')
#         total += 1
#     else:
#         print(f'\033[31m{c}\033[m', end=' ')
# print(f'\nThe number {n} was divided {total} times!')

# if total == 2:
#     print('And that is why it is a PRIME number!')
# else:
#     print('And that is why it is not a PRIME number!')
