import os

def dobro(num: int):
    return num*2

while True:
    print("\n1 - Número par ou ímpar.\n2 - Loop de 1 a 10.\n3 - Dobro do número.\n0 - Parar")
    opcao = int(input("\nDigite uma opcao: "))
    while opcao not in [0, 1, 2, 3]:
        opcao = int(input("\nDigite uma opcao: "))

    if opcao == 0:
        break
    
    if opcao == 1:
        num = int(input("\nDigite um número: "))
        if(num%2 == 0):
            print("\nO número digitado é par.")
        else:
            print("\nO número digitado é ímpar.")
        input("\n")
        os.system('cls')

    elif opcao == 2:
        print()
        for i in range(1, 11):
            if(i%3 != 0):
                print(i)
        input("\n")
        os.system('cls')
    
    elif opcao == 3:
        num = int(input("\nDigite um número: "))
        print(f"\nO dobro de {num} é igual a {dobro(num)}.")
        input("\n")
        os.system('cls')
