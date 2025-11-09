import json

def escrever_json():
    try:
        nome_arquivo = input("Digite o nome do arquivo a ser CRIADO (ex: dados.json): ")  
        
        if not nome_arquivo.endswith('.json'):
            nome_arquivo += '.json'
        
        print("\nPor favor, insira os novos dados:")
        nome = input("Nome: ")
        cidade = input("Cidade: ")
        
        idade = 0
        try:
            idade_input = input("Idade: ")
            idade = int(idade_input)
        except ValueError:
            print(f"Aviso: '{idade_input}' não é um número. Idade será salva como 0.")
            
        pessoa = {
            "nome": nome,
            "idade": idade,
            "cidade": cidade
        }

        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(pessoa, f, indent=4, ensure_ascii=False)
            
        print(f"\nSucesso! Dados escritos em '{nome_arquivo}'.")

    except IOError as e:
        print(f"\nErro ao escrever no arquivo: {e}")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

def modificar_json():
    try:
        nome_arquivo = input("Digite o nome do arquivo a ser MODIFICADO (ex: dados.json): ")       

        if not nome_arquivo.endswith('.json'):
            nome_arquivo += '.json'
        
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            
        print("\n--- Dados Atuais no Arquivo ---")
        print(dados)
        print("---------------------------------")
        
        print("Digite os novos valores (Aperte Enter para manter o valor atual):")
        
        nome_atual = dados.get('nome', '')
        idade_atual = dados.get('idade', 0)
        cidade_atual = dados.get('cidade', '')

        nome = input(f"Nome [{nome_atual}]: ") or nome_atual
        cidade = input(f"Cidade [{cidade_atual}]: ") or cidade_atual
        
        idade_input = input(f"Idade [{idade_atual}]: ")
        if idade_input == "":
            idade = idade_atual
        else:
            try:
                idade = int(idade_input)
            except ValueError:
                print(f"Aviso: '{idade_input}' não é um número. Mantendo a idade original: {idade_atual}")
                idade = idade_atual

        dados_atualizados = {
            "nome": nome,
            "idade": idade,
            "cidade": cidade
        }

        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_atualizados, f, indent=4, ensure_ascii=False)
            
        print(f"\nSucesso! Arquivo '{nome_arquivo}' foi modificado.")

    except FileNotFoundError:
        print(f"\nErro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"\nErro: O arquivo '{nome_arquivo}' não contém um JSON válido.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

def ler_json():
    try:
        nome_arquivo = input("Digite o nome do arquivo a ser LIDO (ex: dados.json): ") 
    
        if not nome_arquivo.endswith('.json'):
            nome_arquivo += '.json'
        
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados_lidos = json.load(f)
            
        print(f"\n--- Dados lidos de '{nome_arquivo}' ---")
        print(f"Nome: {dados_lidos.get('nome', 'Não informado')}")
        print(f"Idade: {dados_lidos.get('idade', 'Não informado')}")
        print(f"Cidade: {dados_lidos.get('cidade', 'Não informado')}")

    except FileNotFoundError:
        print(f"\nErro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"\nErro: O arquivo '{nome_arquivo}' não contém um JSON válido ou está vazio.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

def main():
    while True:
        print("\n--- Gerenciador de Arquivos JSON ---")
        print("1: Escrever um NOVO arquivo")
        print("2: Modificar um arquivo existente")
        print("3: Ler um arquivo existente")
        print("4: Sair")
        
        escolha = input("Digite sua escolha (1, 2, 3 ou 4): ")
        
        if escolha == '1':
            escrever_json()
        elif escolha == '2':
            modificar_json()
        elif escolha == '3':
            ler_json()
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()