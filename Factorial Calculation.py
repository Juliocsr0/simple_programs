# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# from math import factorial
# n = int(input('Digite um numero para ver seu fatorial: '))
# print(f'{factorial(n)}\n')

n = int(input('Digite um numero: '))
c = n
f = 1
print(f'Calculando fatorial de {n}!: ')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

#IF YOU WANT IT IN ENGLISH, just remove the #

#-----------------------------------------------------------------------------------------------------------------------

# Create a program that reads any number and shows its factorial.

# from math import factorial
# n = int(input('Enter a number to see its factorial: '))
# print(f'{factorial(n)}\n')

# n = int(input('Enter a number: '))
# c = n
# f = 1
# print(f'Calculating the factorial of {n}!: ')
# while c > 0:
#     print(f'{c}', end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
# print(f'{f}')