valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

print("--- Resultado da Conversão ---")
print(f"Valor original: R$ {valor_reais:.2f}")
print("------------------------------")
print(f"Valor em Dólares (USD): $ {valor_dolares:.2f}")
print(f"Valor em Euros (EUR): € {valor_euros:.2f}")