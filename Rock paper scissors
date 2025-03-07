# Crie um programa que faça o computador jogar Pedra, Papel e Tesoura com você.

from random import randint
green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
white = '\033[97m'
end = '\033[m'

print(f'{green}-=-{end}' * 20)
print(f'{white}GAME: PEDRA, PAPEL E TESOURA')
print(f'{green}-=-{end}' * 20)
print('\n[ 0 ] Pedra \n[ 1 ] Papel \n[ 2 ] Tesoura')

itens = ('PEDRA', 'PAPEL', 'TESOURA')
maquina = randint(0, 2)
escolha = int(input('\nEscolha uma das opções acima: '))
print(f'A sua escolha foi: {escolha}\n')
if maquina == 0: #Maquina escolheu PEDRA
        if escolha == 0:
                print(f'Eu escolhi PEDRA. {yellow}EMPATE{end}!')
        elif escolha == 1:
                print(f'Eu escolhi PEDRA. Você {green}GANHOU{end}!')
        elif escolha == 2:
                print(f'Eu escolhi PEDRA. Você {red}PERDEU{end}!')
        else:
                print('Opção inválida. Tente novamente.')
if maquina == 1: #Maquina escolhe PAPEL
                if escolha == 1:
                        print(f'Eu escolhi PAPEL. {yellow}EMPATE{end}!') 
                elif escolha == 0:
                        print(f'Eu escolhi PAPEL. Você {red}PERDEU{end}!')
                elif escolha == 2:
                        print(f'Eu escolhi PAPEL. Você {green}GANHOU{end}!')
                else:
                        print('Opção inválida. Tente novamente.')
                    
if maquina == 2: #Maquina escolhe TESOURA
                if escolha == 2:
                        print(f'Eu escolhi TESOURA. {yellow}EMPATE{end}!')
                elif escolha == 0:
                        print(f'Eu escolhi TESOURA. Você {red}PERDEU{end}!')
                elif escolha == 1:
                        print(f'Eu escolhi TESOURA. Você {green}GANHOU{end}!')
                else:
                        print('Opção inválida. Tente novamente.')
                        
#IF YOU WANT IT IN ENGLISH, just remove the #

#------------------------------------------------------------------------------------------------

# Create a program that makes the computer play Rock, Paper, Scissors with you.

# # from random import randint
# # green = '\033[32m'
# red = '\033[31m'
# yellow = '\033[33m'
# white = '\033[97m'
# end = '\033[m'

# print(f'{green}-=-{end}' * 20)
# print(f'{white}GAME: ROCK, PAPER, SCISSORS')
# print(f'{green}-=-{end}' * 20)
# print('\n[ 0 ] Rock \n[ 1 ] Paper \n[ 2 ] Scissors')

# itens = ('ROCK', 'PAPER', 'SCISSORS')
# maquina = randint(0, 2)
# escolha = int(input('\nChoose one of the options above: '))
# print(f'Your choice was: {escolha}\n')
# if maquina == 0: # Machine chose ROCK
#         if escolha == 0:
#                 print(f'I chose ROCK. {yellow}DRAW{end}!')
#         elif escolha == 1:
#                 print(f'I chose ROCK. You {green}WON{end}!')
#         elif escolha == 2:
#                 print(f'I chose ROCK. You {red}LOST{end}!')
#         else:
#                 print('Invalid option. Try again.')
# if maquina == 1: # Machine chose PAPER
#                 if escolha == 1:
#                         print(f'I chose PAPER. {yellow}DRAW{end}!') 
#                 elif escolha == 0:
#                         print(f'I chose PAPER. You {red}LOST{end}!')
#                 elif escolha == 2:
#                         print(f'I chose PAPER. You {green}WON{end}!')
#                 else:
#                         print('Invalid option. Try again.')
                    
# if maquina == 2: # Machine chose SCISSORS
#                 if escolha == 2:
#                         print(f'I chose SCISSORS. {yellow}DRAW{end}!')
#                 elif escolha == 0:
#                         print(f'I chose SCISSORS. You {red}LOST{end}!')
#                 elif escolha == 1:
#                         print(f'I chose SCISSORS. You {green}WON{end}!')
#                 else:
#                         print('Invalid option. Try again.')