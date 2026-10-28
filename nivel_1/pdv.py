# PDV - Desafio Nivel 1

compras = []

print("===== PDV - CAIXA =====")
print("Digite 0 no valor para fechar o caixa\n")

while True:
    valor = float(input("Valor da compra: R$ ").replace(",", "."))

    if valor == 0:
        break

    if valor < 0:
        print("Valor nao pode ser negativo, digite de novo.\n")
        continue

    idade = int(input("Idade do cliente: "))

    if idade < 0:
        print("Idade nao pode ser negativa, digite a compra de novo.\n")
        continue

    qtd = input("Quantidade de itens (enter = 1): ").strip()
    
    if qtd == "":
        qtd = 1
    else:
        qtd = int(qtd)

    if qtd < 1:
        print("Quantidade invalida, digite a compra de novo.\n")
        continue

    cupom = input("Cupom (enter se nao tiver): ").strip().upper()

    valor_final = valor
    descontos = []

    if idade >= 65:
        valor_final = round(valor_final * 0.8, 2)
        descontos.append("idade 20%")

    if valor_final > 100:
        valor_final = round(valor_final * 0.9, 2)
        descontos.append("valor 10%")

    if qtd > 3:
        valor_final = round(valor_final * 0.95, 2)
        descontos.append("quantidade 5%")

    if cupom == "FIDELIDADE10":
        valor_final = round(valor_final * 0.9, 2)
        descontos.append("cupom 10%")
    elif cupom != "":
        print("Cupom invalido, seguindo sem ele.")

    desconto = round(valor - valor_final, 2)

    if len(descontos) > 0:
        print("Descontos:", ", ".join(descontos))
    else:
        print("Sem desconto")

    print(f"Valor final: R$ {valor_final:.2f}\n")

    compras.append({
        "valor": valor,
        "idade": idade,
        "qtd": qtd,
        "final": valor_final,
        "desconto": desconto,
    })

print("\n===== RESUMO DO DIA =====")

if len(compras) == 0:
    print("Nenhuma compra registrada.")
else:
    total_bruto = 0
    total_desconto = 0
    total_final = 0

    for compra in compras:
        total_bruto += compra["valor"]
        total_desconto += compra["desconto"]
        total_final += compra["final"]

    print("Compras registradas:", len(compras))
    print(f"Total bruto: R$ {total_bruto:.2f}")
    print(f"Total de descontos: R$ {total_desconto:.2f}")
    print(f"Total final: R$ {total_final:.2f}")

    with open("resumo.txt", "w") as arquivo:
        arquivo.write("RESUMO DO DIA\n\n")
        n = 1

        for compra in compras:
            arquivo.write(f"{n}. R$ {compra['valor']:.2f} | idade {compra['idade']} | "
                          f"qtd {compra['qtd']} | desconto R$ {compra['desconto']:.2f} | "
                          f"final R$ {compra['final']:.2f}\n")
            n += 1

        arquivo.write(f"\nCompras registradas: {len(compras)}\n")
        arquivo.write(f"Total bruto: R$ {total_bruto:.2f}\n")
        arquivo.write(f"Total de descontos: R$ {total_desconto:.2f}\n")
        arquivo.write(f"Total final: R$ {total_final:.2f}\n")

    print("\nResumo salvo em resumo.txt")
