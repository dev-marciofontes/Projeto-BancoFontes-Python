login = """
#### BANCO FONTES SA  ####
######### LOGIN  #########
"""

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
numero_tentativas =0
LIMITE_TENTATIVAS =3
LIMITE_SAQUES = 3

clientes = {
    1111: {"nome": "Guilherme", "telefone": "3333-2221", "senha":1234},
    2222: {"nome": "Giovanna", "telefone": "3443-2121", "senha":2345},
    3333: {"nome": "Chappie", "telefone": "3344-9871", "senha":3456},
    4444: {"nome": "Melaine", "telefone": "3333-7766", "senha":4567},
}

def validar_login(numero_conta, senha, clientes):
    if numero_conta in clientes and clientes[numero_conta]["senha"] == senha:
        return True
    else:
        return False

while True:
    print(login)
    numero_conta = int(input("Digite o número da sua conta: "))
    senha = int(input("Digite a sua senha: "))

    if validar_login(numero_conta, senha, clientes):
        print("Login realizado com sucesso!\n")
        print(f"Olá {clientes[numero_conta]['nome']}! O que deseja fazer hoje?")
        numero_tentativas = 0
        
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
                print("\nSaindo do sistema...")
                break

            else:
                print("Opção inválida! Selecione novamente uma operação...")

    else:
        numero_tentativas += 1
        if numero_tentativas >= LIMITE_TENTATIVAS:
            print("Você excedeu o número de tentativas. Sua conta foi bloqueada. Por favor, entre em contato com o gerente.")
            break
        else:
            print(f"Senha incorreta. Tentativas restantes: {LIMITE_TENTATIVAS - numero_tentativas}")

print("Obrigado por escolher o nosso banco!")