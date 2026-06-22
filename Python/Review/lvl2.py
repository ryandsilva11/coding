import os

while True:
    print("\n1 - Maior e menor.\n2 - Digitar nomes.\n3 - Cadastrar pessoas\n0 - Parar.")
    opcao = int(input("\nDigite uma opcao: "))
    while opcao not in [0, 1, 2, 3]:
        opcao = int(input("\nDigite uma opcao: "))
    print()
    
    if opcao == 0:
        break

    if opcao == 1:
        nums = []
        
        for i in range(0, 5):
            nums.append(int(input(f"Digite o {i+1}º número: ")))
        maior = nums[0]
        menor = nums[0]
        for i in nums:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
        print(f"\nO maior número da lista é {maior}\n\nO menor número da lista é {menor}")
        input()
        os.system('cls')
        
    if opcao == 2:
        nomes = []
        while True:
            nome = str(input("Digite um nome [Digite SAIR para sair]: ")).lower()
            if nome == "sair":
                break
            nomes.append(nome)
        print("\nNomes digitados: \n")
        for i in nomes:
            print(f"{i}")
        input()
        os.system('cls')
        
    if opcao == 3:
        pessoas = []
        while True:
            temp = {}
            temp["nome"] = str(input("Digite um nome: "))
            temp["idade"] = int(input("Digite uma idade: "))
            temp["cidade"] = str(input("Digite uma cidade: "))
            print()
            pessoas.append(temp)
            while True:
                resp = str(input("Deseja continuar [S/N]?: ")).lower()
                print()
                if resp == "s" or resp == "n":
                    break
            if resp == "n":
                break
        for pessoa in pessoas:
            for key in pessoa:
                if isinstance(pessoa[key], str):
                    pessoa[key] = pessoa[key].capitalize()
                print(f"{key.capitalize()}: {pessoa[key]}")
            print()
        input()
        os.system('cls')
