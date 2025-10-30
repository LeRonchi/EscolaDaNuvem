print("Digite o número do funcionário:")
numero_funcionario = int(input())
print("Digite a quantidade de horas trabalhadas:")
horas_trabalhadas = int(input())
print("Digite o valor recebido por hora (ex: 15.50):")
valor_por_hora = float(input())

salario = horas_trabalhadas * valor_por_hora

print("---------------------------------")
print(f"NUMERO = {numero_funcionario}")
print(f"SALARIO = R$ {salario:.2f}")
