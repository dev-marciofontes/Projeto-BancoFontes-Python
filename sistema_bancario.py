import textwrap

def menu_login():
    login = """\n
    ########## BANCO FONTES SA  ##########
    ===============  MENU  ===============
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [sb]\tServiços Bancários
    [q]\tSair
    Digite a sua opção => """
    return input(textwrap.dedent(login))

def autenticar_login(contas, tentativas):
    while tentativas > 0:
        numero_conta = input("Informe o número da conta: ")
        senha = input("Informe a senha: ")

        for conta in contas:
            if conta["numero_conta"] == numero_conta and conta["senha"] == senha:
                return conta

        tentativas -= 1
        print(f"\n@@@ Credenciais incorretas! Tentativas restantes: {tentativas} @@@")

    return None

def menu():
    menu = """\n
    ########## BANCO FONTES SA  ##########
    ============== SERVIÇOS ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    Digite a sua opção => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t+ R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t- R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, senha, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "senha": senha, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    LIMITE_TENTATIVAS = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu_login()

        if opcao == "nc":
            numero_conta = input("Informe o número da conta: ")
            senha = input("Informe a senha: ")
            conta = criar_conta(AGENCIA, numero_conta, senha, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "lg":
            conta_logada = autenticar_login(contas, LIMITE_TENTATIVAS)
            if conta_logada:
                print(f"\n== Bem-vindo(a), {conta_logada['usuario']['nome']}! ==")
                while True:
                    opcao = menu()

                    if opcao == "d":
                        valor = float(input("Informe o valor do depósito: "))
                        saldo, extrato = depositar(saldo, valor, extrato)

                    elif opcao == "s":
                        valor = float(input("Informe o valor do saque: "))
                        saldo, extrato = sacar(
                            saldo=saldo,
                            valor=valor,
                            extrato=extrato,
                            limite=limite,
                            numero_saques=numero_saques,
                            limite_saques=LIMITE_SAQUES,
                        )

                    elif opcao == "e":
                        exibir_extrato(saldo, extrato=extrato)

                    elif opcao == "q":
                        print("Voltando para o menu anterior...\n")
                        break

                    else:
                        print("Operação inválida, por favor selecione novamente a operação desejada.")
            else:
                print("\n@@@ Acesso negado, retornando ao menu principal. @@@")
                continue

        elif opcao == "q":
            print("Sistema encerrando... Obrigado por usar o Banco Fontes SA!!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
