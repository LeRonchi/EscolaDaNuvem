try:
    print("Digite as 4 notas (N1 N2 N3 N4) com uma casa decimal, separadas por espaço:")
    notas = list(map(float, input().split()))
    
    if len(notas) < 4:
        raise ValueError("Número insuficiente de notas.")
        
    n1, n2, n3, n4 = notas[0], notas[1], notas[2], notas[3]

except ValueError as e:
    print(f"Erro na entrada de dados: {e}. Certifique-se de digitar 4 números válidos.")
    exit()

peso1, peso2, peso3, peso4 = 2, 3, 4, 1
soma_pesos = peso1 + peso2 + peso3 + peso4

soma_produtos = (n1 * peso1) + (n2 * peso2) + (n3 * peso3) + (n4 * peso4)
media_inicial = soma_produtos / soma_pesos

print(f"Media: {media_inicial:.1f}")

if media_inicial >= 7.0:
    print("Aluno aprovado.")

elif media_inicial < 5.0:
    print("Aluno reprovado.")

else:
    print("Aluno em exame.")
    
    try:
        nota_exame = float(input("Digite a nota do exame: "))
    except ValueError:
        print("Erro: Nota do exame deve ser um número válido.")
        exit()

    print(f"Nota do exame: {nota_exame:.1f}")

    media_final = (media_inicial + nota_exame) / 2

    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {media_final:.1f}")