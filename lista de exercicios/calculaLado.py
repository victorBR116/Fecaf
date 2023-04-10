import math

lado1 = float(input("Digite o valor do primeiro lado do cômodo (em metros): "))
lado2 = float(input("Digite o valor do segundo lado do cômodo (em metros): "))

diagonal = math.sqrt(lado1 ** 2 + lado2 ** 2)

print(f"A diagonal do cômodo é de {diagonal:.2f} metros.")
