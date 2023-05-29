valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20

salario_liquido = salario_bruto - ir - sindicato

print("Folha de Pagamento")
print("------------------")
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"(-) IR: R${ir:.2f}")
print(f"(-) Sindicato: R${sindicato:.2f}")
print(f"FGTS: R${fgts:.2f}")
print(f"Total de descontos: R${ir + sindicato:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")
