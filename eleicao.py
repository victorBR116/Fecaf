cont = 0
cont_Victor = 0
cont_Leo = 0
cont_Eweverton = 0
cont_voto_nulo = 0
cont_voto_branco = 0
c = 's'

while c == 's':
    print('Candidatos disponíveis:')
    print('Victor = 13.')
    print('Leo = 42.')
    print('Eweverton = 24.')
    print('Voto Branco = 1.')
    print('Voto nulo (nenhuma das opções acima).')

    digito_eleitoral = int(input('Digite o dígito de seu candidato: '))

    if digito_eleitoral == 13:
        cont_Victor += 1
    elif digito_eleitoral == 42:
        cont_Leo += 1
    elif digito_eleitoral == 24:
        cont_Eweverton += 1
    elif digito_eleitoral == 1:
        cont_voto_branco += 1
    else:
        cont_voto_nulo += 1

    cont += 1
    c = input('Digite S para continuar: ').lower()

print('Victor:', cont_Victor, 'votos,', round(cont_Victor / cont * 100), '% dos votos.')
print('Leo:', cont_Leo, 'votos,', round(cont_Leo / cont * 100), '% dos votos.')
print('Eweverton:', cont_Eweverton, 'votos,', round(cont_Eweverton / cont * 100), '% dos votos.')
print('Brancos:', cont_voto_branco, 'votos,', round(cont_voto_branco / cont * 100), '% dos votos.')
print('Nulos:', cont_voto_nulo, 'votos,', round(cont_voto_nulo / cont * 100), '% dos votos.')
print('Total de votos:', cont,'.')
