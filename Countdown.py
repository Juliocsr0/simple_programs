#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

n = int(input('Digite 1 para iniciar a contagem dos fogos: '))
if n == 1:
    for c in range(10, -1, -1):
        sleep(0.5)
        print(c)
    print('\nKABUMMMMMMMMMMMMMMM\n')
    
else:
    print('Você não digitou um número válido. Tente novamente.')
    
#IF YOU WANT IT IN ENGLISH, just remove the #

#------------------------------------------------------------------------------------------------------------------

# Create a program that displays a countdown for fireworks, going from 10 to 0, with a 1-second pause between them.
# from time import sleep

# n = int(input('Enter 1 to start the fireworks countdown: '))
# if n == 1:
#     for c in range(10, -1, -1):
#         sleep(0.5)
#         print(c)
#     print('\nKABOOMMMMMMMMMMMMMMM\n')
    
# else:
#     print('You did not enter a valid number. Try again.')