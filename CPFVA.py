def valida_cpf(cpf: str) -> bool:
    """
    Função que recebe um CPF como string e verifica se ele é válido.
    Retorna True se o CPF é válido e False caso contrário.
    """
    cpf = cpf.replace(".", "").replace("-", "")  # Remove pontos e traços
    if not cpf.isdigit() or len(cpf) != 11:  # Verifica se o CPF possui 11 dígitos numéricos
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
    # Verifica se os dígitos verificadores são iguais aos informados no CPF
    return cpf[-2:] == f"{digito1:02d}{digito2:02d}"

cpf = "113.747.448-32"
if valida_cpf(cpf):
    print(f"O CPF {cpf} é válido!")
else:
    print(f"O CPF {cpf} é inválido!")
