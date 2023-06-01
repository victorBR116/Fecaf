valor_mercadoria = float(input("Valor da mercadoria: R$ "))
valor_pago = float(input("Valor pago: R$ "))

troco = valor_pago - valor_mercadoria

if troco < 0:
    print(f"Faltam R$ {abs(troco):.2f}")
elif troco == 0:
    print("Não existe troco!")
else:
    notas_moedas = {
        2.00: 0,
        1.00: 0,
        0.50: 0,
        0.25: 0,
        0.10: 0,
        0.05: 0,
        0.01: 0
    }

    for valor in notas_moedas.keys():
        while troco >= valor:
            notas_moedas[valor] += 1
            troco -= valor

    print("Troco: R$", round(valor_pago - valor_mercadoria, 2))
    for nota_moeda, quantidade in notas_moedas.items():
        if quantidade > 0:
            if nota_moeda >= 2.00:
                print(f"{quantidade} Nota(s) de R$ {nota_moeda:.2f}")
            else:
                print(f"{quantidade} Moeda(s) de R$ {nota_moeda:.2f}")
