from time import sleep

print(f"""
{"_-"*7} Bem vindo ao Banco da Valve {"_-"*7}

1 - SALDO
2 - DEPOSITAR
3 - SACAR
4 - EXTRATO
0 - encerrar
{"_-"*28}
""")
saldo, saques = 0, 0
while True:
    opcao = int(input("Qual das opções você deseja: "))
    if opcao > -1 and opcao < 5:
        print(opcao)
        if opcao == 1:
            print(f"Seu saldo atual é de R${saldo:.2f}")

        elif opcao == 2:
            depositar = int(input("Qual o valor do depósito? "))
            print(f"Você depositou {depositar:.2f}")
            saldo += depositar

        elif opcao == 3:
            saques += 1
            if saques == 4:
                print("você ja sacou 3 vezes hoje, volte novamente amanhã.")
                break
            sacar = int(input(f"Quanto deseja sacar?"))
            if saldo >= sacar:
                print(f"Você sacou {sacar:.2f} e você tem {saldo - sacar} na sua conta")
                saldo -= sacar
            else:
                print("operação inválida, você não pode ficar com o saldo negativo")

        elif opcao == 4:
            print(f"você tem ao todo R${saldo:.2f}")

        elif opcao == 0:
            print("Volte sempre")
            sleep(1.5)
            break
    else:
        print("VOCÊ NÃO DIGITOU UMA OPÇÃO VÁLIDA. tente novamente")
        print(opcao)
        continue
