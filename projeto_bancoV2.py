from time import sleep
cadastrado = []
lista_cadastro = []
cadastro = []
numero_conta = 0
menu1 =(f"""
{"_-"*7} Bem vindo ao Banco da Valve {"_-"*7}

1 - já tenho cadastro!
2 - Quero me cadastrar!
0 - Terminar o programa...

{"_-"*28}\n""")
while True:
    print(menu1)
    escolha = int(input("Escolha uma dessa opções: "))
    if escolha == 1:
        cpf_cadastrado = str(input("Digite seu CPF: "))
        if cpf_cadastrado in lista_cadastro: #continuar
            print(f"Bem vindo novamente {lista_cadastro[cpf_cadastrado]}")
        else:
            menu1
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
            if opcao > -1 and opcao < 6:
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
    elif escolha == 2:
        cpf = str(input("Informe o seu CPF: "))
        nome = str(input("Informe seu nome: "))
        idade = int(input("Informe sua idade: "))
        estado = str(input("Informe seu estado: "))

        def cadastar(cpf,nome,idade,estado,numero_conta):
            cadastro.append({"cpf":cpf})
            cadastro.append({"nome":nome})
            cadastro.append({"idade":idade})
            cadastro.append({"estado":estado})
            cadastrado.append(numero_conta)
            lista_cadastro = cadastro.copy()
            cadastrado.append(lista_cadastro)
            cadastro.clear()
            print(lista_cadastro)

        numero_conta += 1
        numero_conta2 = str(numero_conta)
        lista_cadastro.append(numero_conta2)
        cadastar(cpf,nome,idade,estado,numero_conta)
        print(f"obrigado por se cadastrar em nosso banco Sr/Sra: {nome}")
        print(f"Seu CPF É : {cpf}, sua idade é {idade}, e você mora em {estado}")
        print(cadastrado)     

    elif escolha == 0:
        break

    else:
        print("VOCÊ NÃO DIGITOU UMA OPÇÃO VÁLIDA. tente novamente") 
 
print(lista_cadastro)
print("fim do programa")