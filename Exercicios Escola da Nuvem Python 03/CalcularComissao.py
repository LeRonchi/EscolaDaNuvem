try:
    nome_vendedor = input("Digite o nome do vendedor: ")
    salario_fixo = float(input("Digite o salário fixo (ex: 1500.00): "))
    vendas_total = float(input("Digite o total de vendas do mês (ex: 5000.00): "))
except ValueError:
    print("Erro: Por favor, digite números válidos para salário e vendas.")
    exit()

TAXA_COMISSAO = 0.15

valor_comissao = vendas_total * TAXA_COMISSAO

total_a_receber = salario_fixo + valor_comissao

print("\n--- Relatório Final ---")
print(f"Vendedor: {nome_vendedor}")
print(f"TOTAL A RECEBER = R$ {total_a_receber:.2f}")