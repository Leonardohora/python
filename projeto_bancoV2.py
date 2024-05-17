from time import sleep
lista_cadastro = []
numero_conta = 0
conta_encontrada = None
menu1 = (f"""
{"_-"*7} Bem vindo ao Banco da Valve {"_-"*7}

1 - já tenho cadastro!
2 - Quero me cadastrar!
0 - Terminar o programa...

{"_-"*28}\n""")

def cadastrar(cpf, nome, idade, estado, numero_conta):
            cadastro = {
                "cpf": cpf,
                "nome": nome,
                "idade": idade,
                "estado": estado,
                "numero_conta": numero_conta,
                "saldo": 0,
                "limite_saques": 0,
                "extrato": []
            }
            lista_cadastro.append(cadastro)
            print(cadastro)


def deposito(depositar, conta_encontrada, /):
        print(f"Você depositou R${depositar:.2f}")
        conta_encontrada['saldo'] += depositar
        conta_encontrada['extrato'].append(f"Depósito: +R${depositar:.2f}")


def saque(*, conta_encontrada, sacar):
    conta_encontrada['saldo'] -= sacar
    conta_encontrada['limite_saques'] += 1
    conta_encontrada['extrato'].append(f"Saque: -R${sacar:.2f}")


def extrato(conta_encontrada):
    for transacao in conta_encontrada['extrato']:
        print(transacao)


while True:
    print(menu1)
    escolha = int(input("Escolha uma dessas opções: "))
    if escolha == 1:
        cpf_cadastrado = str(input("Digite seu CPF: "))
        for lista_cpf in lista_cadastro:
            if lista_cpf.get("cpf") == cpf_cadastrado:
                conta_encontrada = lista_cpf
                print(f"Bem-vindo novamente, {lista_cpf['nome']}")
                break

        if not conta_encontrada:
            print("CPF não encontrado. Tente novamente ou faça o cadastro.")
            continue
        
        menu = (f"""
        {"_-"*7} Bem vindo ao Banco da Valve {"_-"*7}

        1 - SALDO
        2 - DEPOSITAR
        3 - SACAR
        4 - EXTRATO
        0 - encerrar

        {"_-"*28}\n""")

        sleep(2)
        
        while True:
            print(menu)
            opcao = int(input("Qual das opções você deseja: "))
            
            if opcao > -1 and opcao < 5:
                if opcao == 1:
                    print(f"Seu saldo atual é de R${conta_encontrada['saldo']:.2f}")
                    sleep(1.5)

                elif opcao == 2:
                    depositar = float(input("Qual o valor do depósito? "))
                    if depositar < 1:
                        print("Você não pode depositar valores abaixo de R$1,00")
                        sleep(1.5)
                    else:
                        deposito(depositar, conta_encontrada)
                        sleep(1.5)

                elif opcao == 3:
                    if conta_encontrada['limite_saques'] == 3:
                        print("Você já sacou 3 vezes hoje, volte novamente amanhã.\n")
                        sleep(2)

                    else:
                        sacar = float(input(f"Quanto deseja sacar? "))
                        if sacar > 500:
                            print("Você só pode sacar valor abaixo ou igual a R$500,00 \n")
                            sleep(1.5)

                        elif conta_encontrada['saldo'] >= sacar:
                            saque(conta_encontrada=conta_encontrada, sacar=sacar)
                            sleep(1.5)

                        else:
                            print("Operação INVÁLIDA, você não pode ficar com o saldo NEGATIVO \n")
                            sleep(2)

                elif opcao == 4:
                    print(f"Seu extrato é:\n")
                    sleep(1)
                    extrato(conta_encontrada)
                    sleep(1.5)

                elif opcao == 0:
                    print("Volte sempre")
                    break
            else:
                print("VOCÊ NÃO DIGITOU UMA OPÇÃO VÁLIDA. Tente novamente")
                sleep(2)
    
    elif escolha == 2:
        cpf = str(input("Informe o seu CPF: "))
        nome = str(input("Informe seu nome: "))
        idade = int(input("Informe sua idade: "))
        estado = str(input("Informe seu estado: "))

        numero_conta += 1
        cadastrar(cpf, nome, idade, estado, numero_conta)
        
        print(f"""Obrigado por se cadastrar em nosso banco Sr/Sra: {nome}
                  Seu CPF é: {cpf}, sua idade é {idade}, e você mora em {estado}
                  O Numero da sua conta é {numero_conta}""")


    elif escolha == 0:
        break

    else:
        print("VOCÊ NÃO DIGITOU UMA OPÇÃO VÁLIDA. Tente novamente") 

print("Essas são as listas dos cadastrado:")
for mostrar in lista_cadastro:
    print(mostrar)

print("Fim\ndo\nprograma")