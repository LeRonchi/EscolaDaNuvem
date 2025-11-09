import csv

nome_arquivo = 'dados_pessoais.csv'

try:
    with open(nome_arquivo, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        print(f"\nConteúdo do arquivo '{nome_arquivo}':")
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Certifique-se de que ele foi criado e está no local correto.")
except Exception as e:
    print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")