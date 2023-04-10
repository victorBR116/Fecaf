# Ler o número total de eleitores, votos brancos, nulos e válidos
total_eleitores = int(input("Digite o número total de eleitores: "))
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

# Calcular o percentual de votos brancos, nulos e válidos em relação ao total de eleitores
percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100

# Exibir o resultado
print("Percentual de votos brancos: %.2f%%" % percentual_brancos)
print("Percentual de votos nulos: %.2f%%" % percentual_nulos)
print("Percentual de votos válidos: %.2f%%" % percentual_validos)
