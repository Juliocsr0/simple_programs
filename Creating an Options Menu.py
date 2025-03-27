# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Encontrar o Maior Número
# [ 4 ] Inserir Novos Números
# [ 5 ] Sair do Programa

from time import sleep

opcao = 0
while opcao != 5:
    print("=" * 40)
    print("MENU DE OPÇÕES".center(40))
    print("=" * 40)
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Encontrar o Maior Número
    [ 4 ] Inserir Novos Números
    [ 5 ] Sair do Programa
    ''')
    opcao = int(input("Escolha uma opção: "))
    print("=" * 40)

    if opcao == 1:
        print(f"A soma entre {n1} + {n2} = {n1 + n2}")
    elif opcao == 2:
        print(f"A multiplicação entre {n1} x {n2} = {n1 * n2}")
    elif opcao == 3:
        print(f"O maior número entre {n1} e {n2} é {max(n1, n2)}")
    elif opcao == 4:
        print("Inserira novos números...")
    elif opcao == 5:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Por favor, tente novamente.")
    
    sleep(1)  # Adiciona um pequeno atraso para melhorar a experiência do usuário

print("=" * 40)
print("Obrigado por usar o programa. Até logo!")
print("=" * 40)

#IF YOU WANT IT IN ENGLISH, just remove the #

#--------------------------------------------------------------------------------------------------------------------

# Create a program that reads two values and shows a menu on the screen:
# [ 1 ] Add
# [ 2 ] Multiply
# [ 3 ] Find the Largest Number
# [ 4 ] Enter New Numbers
# [ 5 ] Exit the Program

# from time import sleep

# option = 0
# while option != 5:
#     print("=" * 40)
#     print("OPTIONS MENU".center(40))
#     print("=" * 40)
#     n1 = int(input("Enter the first number: "))
#     n2 = int(input("Enter the second number: "))
#     print('''
#     [ 1 ] Add
#     [ 2 ] Multiply
#     [ 3 ] Find the Largest Number
#     [ 4 ] Enter New Numbers
#     [ 5 ] Exit the Program
#     ''')
#     option = int(input("Choose an option: "))
#     print("=" * 40)

#     if option == 1:
#         print(f"The sum of {n1} + {n2} = {n1 + n2}")
#     elif option == 2:
#         print(f"The multiplication of {n1} x {n2} = {n1 * n2}")
#     elif option == 3:
#         print(f"The largest number between {n1} and {n2} is {max(n1, n2)}")
#     elif option == 4:
#         print("Enter new numbers...")
#     elif option == 5:
#         print("Exiting the program...")
#     else:
#         print("Invalid option. Please try again.")
    
#     sleep(1)  # Adds a small delay for better user experience

# print("=" * 40)
# print("Thank you for using the program. Goodbye!")
# print("=" * 40)