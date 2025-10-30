nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

preco_total = preco_unitario * quantidade

print("Resumo da Compra")
print(f"Produto: {nome_produto}")
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade Comprada: {quantidade}")
print("----------------------------------------------------------------" )
print(f"Preço Total (R$ {preco_unitario} x {quantidade}): R$ {preco_total:.2f}")