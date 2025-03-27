# O computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

'''from random import randint

palpite = 0
jogador = 0
computador = randint(0, 10)
print('Eu sou um robo, e estou pensando em um número entre 0 e 10. \nTente adivinhar!')
while jogador != computador:
    jogador = int(input('Digite um número entre 0 e 10: '))
    palpite += 1
    if jogador > computador:
        print('Um pouco menos. Tente de novo: ')
    elif jogador < computador:
        print('Um pouco mais. \nTente de novo')
print(f'Você ganhou! Você tentou adivinhar {palpite} vezes!')''' #that’s one option, but I prefer the one under it.

from random import randint

palpite = 0 
computador = randint(0, 10)
acertou = False

print('Olá, sou o seu computador... vou pensar em um número entre 0 e 10. \nTente adivinhar')
while not acertou:
    jogador = int(input('Digite um numero de 0 a 10: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    if jogador > computador:
        print('Um pouco menos...')
    if jogador < computador:
        print('Um pouco mais...')
print(f'Você \033[32mGANHOU!\033[m. Você acertou com {palpite} tentativas.')

#IF YOU WANT IT IN ENGLISH, just remove the #

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The computer will "think" of a number between 0 and 10.
# The player will try to guess until they get it right, showing at the end how many guesses were needed to win.

'''from random import randint

guess_count = 0
player = 0
computer = randint(0, 10)
print('I am a robot, and I am thinking of a number between 0 and 10. \nTry to guess!')
while player != computer:
    player = int(input('Enter a number between 0 and 10: '))
    guess_count += 1
    if player > computer:
        print('A little less. Try again: ')
    elif player < computer:
        print('A little more. \nTry again')
print(f'You won! It took you {guess_count} guesses!')''' #that’s one option, but I prefer the one under it.

# from random import randint

# guess_count = 0
# computer = randint(0, 10)
# guessed_correctly = False

# print('Hello, I am your computer... I will think of a number between 0 and 10. \nTry to guess!')
# while not guessed_correctly:
#     player = int(input('Enter a number between 0 and 10: '))
#     guess_count += 1
#     if player == computer:
#         guessed_correctly = True
#     if player > computer:
#         print('A little less...')
#     if player < computer:
#         print('A little more...')
# print(f'You \033[32mWON!\033[m. You guessed it in {guess_count} attempts.')