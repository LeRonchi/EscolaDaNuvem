print("Verificador de Ano Bissexto")

try:
    ano = int(input("Digite um ano inteiro (ex: 2024): "))
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
    exit()

e_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

print("-----------------------------------")
print(f"Ano inserido: {ano}")

if e_bissexto:
    print("Resultado: O ano é Bissexto!")
else:
    print("Resultado: O ano NÃO é Bissexto.")