# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Digite uma frase: ').strip().upper()
separada = frase.split()
junta = ''.join(separada)
invert = junta[::-1]
print(f'A frase foi {junta} e o inverso {invert}')
if junta == invert:
    print('A frase digitada é um POLÍNDROMO')
else:
    print('A frase digitada NÃO é um POLÍNDROMO')
    
# IF YOU WANT IT IN ENGLISH, just remove the #

# --------------------------------------------------------------------------------------------------------------------------------------------------
    
# Create a program that reads any phrase and says whether it is a palindrome, disregarding spaces. Examples of palindromes:

# A MAN, A PLAN, A CANAL, PANAMA!, MADAM, IN EDEN, I’M ADAM, NEVER ODD OR EVEN, ABLE WAS I, I SAW ELBA, EVIL IS A NAME OF A FOEMAN, AS I LIVE.

# phrase = input('Enter a phrase: ').strip().upper()
# separated = phrase.split()
# joined = ''.join(separated)
# reversed_phrase = joined[::-1]
# print(f'The phrase was {joined} and the reverse is {reversed_phrase}')
# if joined == reversed_phrase:
#     print('The entered phrase is a PALINDROME')
# else:
#     print('The entered phrase is NOT a PALINDROME')