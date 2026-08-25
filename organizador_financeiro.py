# ==========================================
#       ORGANIZADOR FINANCEIRO 💰
# ==========================================

print("=" * 45)
print("        ORGANIZADOR FINANCEIRO")
print("=" * 45)

nome = input("Olá! Qual é o seu nome? ").title()

print(f"\nOlá, {nome}! Vamos organizar suas finanças 😎\n")

# ------------------------------------------
# ESCOLHA DO PAGAMENTO
# ------------------------------------------

print("Qual pagamento você deseja organizar?")
print("1 - Dia 15")
print("2 - Dia 30")

opcao = input("Escolha: ")

# ------------------------------------------
# RECEBIMENTO
# ------------------------------------------

if opcao == "1":
    pagamento = 15
    salario = float(input("Quanto você recebeu no dia 15? R$ "))

elif opcao == "2":
    pagamento = 30
    salario = float(input("Quanto você recebeu no dia 30? R$ "))

else:
    print("\nOpção inválida!")
    exit()

# ------------------------------------------
# GASTOS FIXOS
# ------------------------------------------

gastos = [
    ["Faculdade", 260.00],
    ["Celular", 119.00],
    ["Pai e mãe", 200.00],
    ["Crédito celular", 35.00]
]

# ------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------

while True:

    print("\n" + "=" * 45)
    print(f" PAGAMENTO DO DIA {pagamento}")
    print("=" * 45)

    print("1 - Ver gastos")
    print("2 - Adicionar gasto")
    print("3 - Remover gasto")
    print("4 - Calcular saldo")
    print("5 - Ver informações do pagamento")
    print("6 - Sair")

    escolha = input("\nEscolha uma opção: ")

    # --------------------------------------
    # VER GASTOS
    # --------------------------------------

    if escolha == "1":

        print("\n========== GASTOS ==========")

        if len(gastos) == 0:
            print("Nenhum gasto cadastrado.")

        else:
            for i, gasto in enumerate(gastos, start=1):

                nome_gasto = gasto[0]
                valor_gasto = gasto[1]

                print(f"{i}. {nome_gasto} - R$ {valor_gasto:.2f}")

    # --------------------------------------
    # ADICIONAR GASTO
    # --------------------------------------

    elif escolha == "2":

        print("\n========== NOVO GASTO ==========")

        nome_gasto = input("Nome do gasto: ").title()
        valor_gasto = float(input("Valor do gasto: R$ "))

        gastos.append([nome_gasto, valor_gasto])

        print(f"\nGasto '{nome_gasto}' adicionado com sucesso!")

    # --------------------------------------
    # REMOVER GASTO
    # --------------------------------------

    elif escolha == "3":

        print("\n========== REMOVER GASTO ==========")

        if len(gastos) == 0:
            print("Não existem gastos para remover.")

        else:

            for i, gasto in enumerate(gastos, start=1):
                print(f"{i}. {gasto[0]} - R$ {gasto[1]:.2f}")

            try:

                numero = int(input("\nDigite o número do gasto que deseja remover: "))

                if 1 <= numero <= len(gastos):

                    removido = gastos.pop(numero - 1)

                    print(f"\nGasto '{removido[0]}' removido com sucesso!")

                else:
                    print("\nNúmero de gasto inválido.")

            except ValueError:
                print("\nDigite apenas um número.")

    # --------------------------------------
    # CALCULAR SALDO
    # --------------------------------------

    elif escolha == "4":

        total_gastos = 0

        for gasto in gastos:
            total_gastos += gasto[1]

        saldo = salario - total_gastos

        print("\n========== RESUMO ==========")
        print(f"Valor recebido: R$ {salario:.2f}")
        print(f"Total de gastos: R$ {total_gastos:.2f}")
        print(f"Saldo restante: R$ {saldo:.2f}")

    # --------------------------------------
    # INFORMAÇÕES
    # --------------------------------------

    elif escolha == "5":

        print("\n========== PAGAMENTO ==========")
        print(f"Nome: {nome}")
        print(f"Pagamento: Dia {pagamento}")
        print(f"Valor recebido: R$ {salario:.2f}")

    # --------------------------------------
    # SAIR
    # --------------------------------------

    elif escolha == "6":

        print(f"\nAté mais, {nome}! 💪")
        break

    else:

        print("\nOpção inválida. Tente novamente.")