def valida_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "") 
    
    if len(cpf) != 11 or not cpf.isdigit(): 
        return False
    
    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    
    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
        
    # Verifica se os dígitos verificadores são iguais aos do CPF informado
    if cpf[-2:] == str(digito1) + str(digito2):
        return True
    else:
        return False

cpf = input("Digite o CPF: ")
if valida_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
