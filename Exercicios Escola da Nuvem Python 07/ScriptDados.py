import csv
import os

nome_arquivo = 'dados_pessoais.csv'

cabecalho = ['Nome', 'Idade', 'Cidade']

precisa_cabecalho = True
if os.path.exists(nome_arquivo):
    if os.path.getsize(nome_arquivo) > 0:
        precisa_cabecalho = False

print("--- Cadastro de Pessoas no CSV ---")
print("Digite 'sair' no campo 'Nome' para parar.")

novos_dados = []

while True:
    print("\nPor favor, insira os dados da nova pessoa:")
    nome = input("Nome: ")
  
    if nome.lower() == 'sair':
        break
        
    idade = input("Idade: ")
    cidade = input("Cidade: ")
    
    novos_dados.append([nome, idade, cidade])

try:
    with open(nome_arquivo, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        if precisa_cabecalho:
            writer.writerow(cabecalho)
        
        if novos_dados:
            writer.writerows(novos_dados)
            print(f"\nSucesso! {len(novos_dados)} nova(s) linha(s) foram adicionadas ao arquivo '{nome_arquivo}'.")
        else:
            print("\nNenhum dado novo foi digitado. O arquivo não foi modificado.")

except IOError as e:
    print(f"Erro ao escrever no arquivo '{nome_arquivo}': {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")