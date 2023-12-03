menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"    
    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! nújmero maximo de saques excedido.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif valor > saldo:
            print("Operação falhou! você não tem saldo suficiente.")
        else:
            numero_saques += 1
            saldo -= valor
            extrato += f"Saque: -R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")    
    elif opcao == "e":
        print("\n*************** EXTRATO ***************\n")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        print("\n***************************************")

    elif opcao == "q":
        break
