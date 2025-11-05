def calcular_preco_com_desconto(preco_original: float, percentual_desconto: float) -> float: 
    if preco_original < 0 or percentual_desconto < 0:
        raise ValueError("Valores de preço e desconto não podem ser negativos.")
        
    valor_do_desconto = preco_original * (percentual_desconto / 100)
    
    preco_final = preco_original - valor_do_desconto
    
    return preco_final

def iniciar_calculadora():
    """Função principal para interagir com o usuário."""
    print("--- Calculadora de Preço Final com Desconto ---")
    
    try:
        preco_input = input("Digite o preço original do produto: ")
        preco_original = float(preco_input)
        
        desconto_input = input("Digite o percentual de desconto: ")
        percentual_desconto = float(desconto_input)
        
        preco_final_calculado = calcular_preco_com_desconto(preco_original, percentual_desconto)
        
        print("\n--- Resultado ---")
        print(f"Preço Original: R$ {preco_original:.2f}")
        print(f"Desconto aplicado: {percentual_desconto:.0f}%")
        print("--------------------")
        print(f"Preço Final: R$ {preco_final_calculado:.2f}")
        
    except ValueError:
        print("\nErro: Valor inválido.")
        print("Por favor, digite apenas números para o preço e o desconto.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    iniciar_calculadora()