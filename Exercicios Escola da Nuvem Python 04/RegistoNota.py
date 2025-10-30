notas_validas = []
soma_notas = 0
contador_notas = 0

print("Registro de Notas (0 a 10)")
print("Digite 'fim' para calcular a média.")

while True:
    entrada = input("Digite a nota do aluno: ").strip().lower()

    if entrada == 'fim':
        break

    try:
        nota = float(entrada)
        
        if 0 <= nota <= 10:
            soma_notas += nota
            contador_notas += 1
            notas_validas.append(nota)
        else:
            print("Aviso: Nota fora do intervalo (0 a 10). Tente novamente.")
            
    except ValueError:
        print("Aviso: Entrada inválida. Digite um número ou 'fim'.")
        
print("\nResultado")

if contador_notas > 0:
    media = soma_notas / contador_notas
    print(f"Total de notas válidas registradas: {contador_notas}")
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")