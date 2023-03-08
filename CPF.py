import re
#validador usando regex
def valida_cpf(cpf: str) -> bool:
    # Remove pontos e traços do CPF
    cpf = re.sub(r'[^\d]+', '', cpf)
    
    # Verifica se o CPF possui 11 dígitos numéricos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if len(set(cpf)) == 1:
        return False
    
    # Verifica se os dois dígitos verificadores estão corretos
    soma = 0
    for i, v in enumerate(cpf[:9]):
        soma += int(v) * (10 - i)
    digito1 = (soma * 10) % 11 % 10
    if cpf[9] != str(digito1):
        return False
    soma = 0
    for i, v in enumerate(cpf[:10]):
        soma += int(v) * (11 - i)
    digito2 = (soma * 10) % 11 % 10
    if cpf[10] != str(digito2):
        return False
    
    # CPF válido
    return True

cpf = "113.747.448-32"
if valida_cpf(cpf):
    print(f"O CPF {cpf} é válido!")
else:
    print(f"O CPF {cpf} é inválido!")
