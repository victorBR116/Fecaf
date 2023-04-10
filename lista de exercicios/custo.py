custo_fabrica = float(input("Digite o custo de fábrica do carro: "))
percentual_distribuidor = 0.28
impostos = 0.45

custo_final = custo_fabrica + (custo_fabrica * percentual_distribuidor) + (custo_fabrica * impostos)

print("O custo final para o consumidor é de R$", custo_final)
