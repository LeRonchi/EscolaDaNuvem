print("--- Calculadora de Índice de Massa Corporal (IMC) ---")

try:
    print("Digite seu peso em quilogramas (ex: 75.5):")
    peso = float(input())

    print("Digite sua altura em metros (ex: 1.78):")
    altura = float(input())
    
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite números válidos para peso e altura.")
    exit()

if altura <= 0 or peso <= 0:
    print("Erro: Peso e altura devem ser valores positivos.")
    exit()


imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
    
elif imc < 25:
    classificacao = "Peso normal"
    
elif imc < 30:
    classificacao = "Sobrepeso"
    
else:
    classificacao = "Obeso"

print("\n--- Resultado do IMC ---")
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")