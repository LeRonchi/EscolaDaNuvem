nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

valor_desconto = preco_original * (percentual_desconto / 100)

preco_final = preco_original - valor_desconto

print(f"Detalhes do Produto: {nome_produto} ")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto de: {percentual_desconto}%")
print("----------------------------------")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final com Desconto: R$ {preco_final:.2f}")