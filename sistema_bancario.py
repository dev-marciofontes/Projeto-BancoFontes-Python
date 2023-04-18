menu = """
#### BANCO FONTES SA  ####
########## MENU ##########

[1] Depositar
[2] Sacar
[3] Extrato
[s] Sair

##########################

Digite a sua opção => """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("##  Depósito  ##")
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(("Depósito", valor_deposito))
        else:
            print("Valor inválido!")

    elif opcao == "2":
        print("##  Saque  ##")
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if (valor_saque > 0 and valor_saque <= limite) and (valor_saque <= saldo):
                saldo -= valor_saque
                extrato.append(("Saque", valor_saque))
                numero_saques += 1
            else:
                print("Valor inválido ou limite de saque atingido!\n")
        else:
            print("Número máximo de saques diários atingido!\n")

    elif opcao == "3":
        print("##  Extrato  ##")
        if len(extrato) == 0:
            print("Não foram realizadas movimentações.")
        else:
            print("\nMovimentações:")
            for operacao, valor in extrato:
                if operacao == "Depósito":
                    print("{}: + R$ {:.2f}".format(operacao, valor))
                else:
                    print("{}: - R$ {:.2f}".format(operacao, valor))    
            print("\nSaldo Atual: R$ {:.2f}\n\n".format(saldo))

    elif opcao == "s":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Selecione novamente uma operação...")

print("Obrigado por escolher o nosso banco!")
