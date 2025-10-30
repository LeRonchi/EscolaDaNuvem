cont_pares = 0
cont_impares = 0

print("Classificador de Paridade")
print("Digite 'fim' a qualquer momento para sair e ver o resultado.")

while True:
    entrada = input("Digite um número inteiro: ").strip().lower()

    if entrada == 'fim':
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            cont_pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            cont_impares += 1

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")
        
print("\n--- Resultado Final ---")
print(f"Números Pares inseridos: {cont_pares}")
print(f"Números Ímpares inseridos: {cont_impares}")