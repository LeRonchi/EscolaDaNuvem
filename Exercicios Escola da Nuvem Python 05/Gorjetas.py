def calcular_e_exibir_gorjetas(valor_conta: float):
    
    if valor_conta < 0:
        print("Erro: O valor da conta não pode ser negativo.")
        return

    gorjeta_15 = valor_conta * (15 / 100)
    gorjeta_15 = round(gorjeta_15, 2)
    total_15 = valor_conta + gorjeta_15

    gorjeta_20 = valor_conta * (20 / 100)
    gorjeta_20 = round(gorjeta_20, 2)
    total_20 = valor_conta + gorjeta_20

    print(f"\n--- Opções de Gorjeta para R$ {valor_conta:.2f} ---")
    print(f"  15%: R$ {gorjeta_15:.2f} (Total: R$ {total_15:.2f})")
    print(f"  20%: R$ {gorjeta_20:.2f} (Total: R$ {total_20:.2f})")

while True:
    try:
        valor_input = input("\nDigite o valor total da conta (ou 's' para sair): R$ ")
        
        if valor_input.lower() == 's':
            print("Saindo...")
            break
            
        valor_da_conta = float(valor_input)
        
        calcular_e_exibir_gorjetas(valor_da_conta)

    except ValueError:
        print("Entrada inválida. Por favor, digite um número (ex: 85.50).")