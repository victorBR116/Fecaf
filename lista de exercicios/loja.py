# lista de lojas
lojas = [("Loja A", [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500]),
         ("Loja B", [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500]),
         ("Loja C", [3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500])]

# somas semestrais
for loja in lojas:
    nome = loja[0]
    vendas_semestre1 = sum(loja[1][:6])
    vendas_semestre2 = sum(loja[1][6:])
    print(f"{nome}: Semestre 1: {vendas_semestre1}, Semestre 2: {vendas_semestre2}")

