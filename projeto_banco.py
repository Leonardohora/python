from time import sleep

menu =(f"""
{"_-"*7} Bem vindo ao Banco da Valve {"_-"*7}

1 - SALDO
2 - DEPOSITAR
3 - SACAR
4 - EXTRATO
0 - encerrar

{"_-"*28}\n""")

sleep(2)
extrato_deposito = ""
extrato_saque = ""
saldo, SAQUES = 0, 0
while True:
    print(menu)
    opcao = int(input("Qual das opções você deseja: "))
    if opcao > -1 and opcao < 5:
        print(opcao)
        if opcao == 1:
            print(f"Seu saldo atual é de R${saldo:.2f}")
            sleep(1.5)

        elif opcao == 2:
            depositar = float(input("Qual o valor do depósito? "))
            if depositar < 1:
                print("Você não pode depositar valores abaixo de R$1,00")
                sleep(1.5)
            else:
                print(f"Você depositou {depositar:.2f}")
                extrato_deposito += str(f"   Depósito: +{depositar}\n")
                saldo += depositar
                sleep(1.5)

        elif opcao == 3:
            if SAQUES == 3:
                print("Você ja sacou 3 vezes hoje, volte novamente amanhã.\n")
                sleep(2)
            else:
                sacar = int(input(f"Quanto deseja sacar?"))
                if sacar > 500:
                    print("Você só pode sacar valor abaixo ou igual a R$500,00 \n")
                    sleep(1.5)
                elif saldo >= sacar:
                    print(f"Você sacou R${sacar:.2f} \n")
                    extrato_saque += str(f"   Saque: -{sacar}\n")
                    saldo -= sacar
                    SAQUES += 1
                else:
                    print("Operação INVÁLIDA, você não pode ficar com o saldo NEGATIVO \n")
                    sleep(2)

        elif opcao == 4:
            print(f"Seu extrato é:\n")
            sleep(1.5)
            print(f"{extrato_deposito}")
            sleep(1.5)
            print(f"{extrato_saque}")

        elif opcao == 0:
            print("Volte sempre")
            break
    else:
        print("VOCÊ NÃO DIGITOU UMA OPÇÃO VÁLIDA. tente novamente")
        sleep(2)

print("FIM DO PROGRAMA")