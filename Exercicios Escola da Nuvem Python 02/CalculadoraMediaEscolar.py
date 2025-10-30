nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

notas = [nota1, nota2, nota3]

soma_das_notas = nota1 + nota2 + nota3
numero_de_notas = 3

media = soma_das_notas / numero_de_notas

print("Boletim Escolar")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print("------------------------")
print(f"Média Final: {media:.2f}")

if media >= 7.0:
    print("Situação: Aprovado!")
elif media >= 5.0:
    print("Situação: Recuperação.")
else:
    print("Situação: Reprovado.")