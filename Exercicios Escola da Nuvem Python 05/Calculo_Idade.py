from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    hoje = date.today()
    data_nascimento_aproximada = date(ano_nascimento, 1, 1)
    diferenca = hoje - data_nascimento_aproximada
    return diferenca.days

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_em_dias = calcular_idade_em_dias(ano_nascimento)
print(f"Com base no ano {ano_nascimento}, a idade aproximada em dias é: {idade_em_dias}")