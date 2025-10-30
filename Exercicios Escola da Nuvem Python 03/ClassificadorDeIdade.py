print("Por favor, digite sua idade em anos (ex: 35):")

try:
    idade = int(input())
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para a idade.")
    exit()

if idade < 0:
    categoria = "Idade Inválida"
    
elif idade <= 12:
    categoria = "Criança"
    
elif idade <= 17:
    categoria = "Adolescente"
    
elif idade <= 59:
    categoria = "Adulto"
    
else:
    categoria = "Idoso"

print("----------------------------")
print(f"Sua idade é: {idade} anos")
print(f"Sua classificação é: {categoria}")