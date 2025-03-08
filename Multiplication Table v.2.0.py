#Mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('\nDigite um número para ver sua taboada: '))
for taboada in range(1, 11):
    soma = n * taboada
    print(f'\n{n} x {taboada} = {soma}')
    
#IF YOU WANT IT IN ENGLISH, just remove the #

#------------------------------------------------------------------------------------------------------------------------
    
# Showing the multiplication table of a number chosen by the user, but now using a for loop.

# n = int(input('Enter a number to see its multiplication table: '))
# for taboada in range(1, 11):
#     result = n * taboada
#     print(f'{n} x {taboada} = {result}')
