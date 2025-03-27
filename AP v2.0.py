# Lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('\nGerador de PA')
print('=-=' * 5)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
passo = termo
contador = 0
while contador < 10:
    contador += 1
    print(f'{passo}', end=' → ')
    passo += razao
print('FIM')

#IF YOU WANT IT IN ENGLISH, just remove the #

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Reading the first term and the common difference of an AP, showing the first 10 terms of the progression using a while loop.

# print('\nAP Generator')
# print('=-=' * 5)
# term = int(input('First term: '))
# difference = int(input('Common difference: '))
# current = term
# counter = 0
# while counter < 10:
#     counter += 1
#     print(f'{current}', end=' → ')
#     current += difference
# print('END')