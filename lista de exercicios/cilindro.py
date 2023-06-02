import math

# Lendo os valores de entrada
raio = float(input("digite o valor do raio do cilindro em cm: "))
altura = float(input("Digite o valor da altura do cilindro em cm: "))

# Calculando a área da base
area_base = math.pi * (raio ** 2)
print("Área da base do cilindro: {:.2f} cm²".format(area_base))

# Calculando a área lateral
area_lateral = 2 * math.pi * raio * altura
print("Área lateral do cilindro: {:.2f} cm²".format(area_lateral))

# Calculando a área total
area_total = 2 * area_base + area_lateral
print("Área total do cilindro: {:.2f} cm²".format(area_total))

# Calculando o volume
volume = area_base * altura
print("Volume do cilindro: {:.2f} cm³".format(volume))
