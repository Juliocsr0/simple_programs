# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10) * razao # Para receber os 10 primeiros termos.
for c in range(termo, decimo, razao):
    print(f'{c}', end=' → ')
print('FIM')

#IF YOU WANT IT IN ENGLISH, just remove the #

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Develop a program that reads the first term and the common difference of an AP (Arithmetic Progression). In the end, show the first 10 terms of this progression.

# term = int(input('First term: '))
# difference = int(input('Common difference: '))
# tenth = term + (11 - 1) * difference # To get the first 10 terms.
# for c in range(term, tenth, difference):
#     print(f'{c}', end=' → ')
# print('END')