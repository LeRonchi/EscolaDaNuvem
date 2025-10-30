def converter_para_celsius(valor, unidade_origem):
    if unidade_origem.upper() == 'C':
        return valor
    elif unidade_origem.upper() == 'F':
        return (valor - 32) / 1.8
    elif unidade_origem.upper() == 'K':
        return valor - 273.15
    else:
        return None

def converter_de_celsius(celsius, unidade_destino):
    if unidade_destino.upper() == 'C':
        return celsius
    elif unidade_destino.upper() == 'F':
        return celsius * 1.8 + 32
    elif unidade_destino.upper() == 'K':
        return celsius + 273.15
    else:
        return None
    
print("Conversor de Temperatura")
print("Unidades suportadas: C (Celsius), F (Fahrenheit), K (Kelvin)")

try:
    valor_origem = float(input("Digite a temperatura: "))
    unidade_origem = input("Digite a unidade de origem (C, F ou K): ").strip().upper()
    unidade_destino = input("Digite a unidade de destino (C, F ou K): ").strip().upper()
    
except ValueError:
    print("Erro: A temperatura deve ser um número válido.")
    exit()

celsius = converter_para_celsius(valor_origem, unidade_origem)

if celsius is None:
    print("Erro: Unidade de origem não reconhecida.")
else:
    valor_final = converter_de_celsius(celsius, unidade_destino)
    if valor_final is None:
        print("Erro: Unidade de destino não reconhecida.")
    else:
        print("\n--- Resultado ---")
        print(f"Temperatura Original: {valor_origem:.2f} {unidade_origem}")
        print(f"Temperatura Convertida: {valor_final:.2f} {unidade_destino}")