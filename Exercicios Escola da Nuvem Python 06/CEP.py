import requests

def consultar_cep():
    cep = input("Digite o CEP (somente números): ")
    
    cep = ''.join(filter(str.isdigit, cep))

    if len(cep) != 8:
        print("CEP inválido. Por favor, digite 8 dígitos numéricos.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        dados_cep = response.json() 
        
        if 'erro' in dados_cep and dados_cep['erro']:
            print(f"CEP '{cep}' não encontrado ou inválido.")
        else:
            print(f"\nInformações para o CEP {cep}:")
            print(f"Logradouro: {dados_cep.get('logradouro', 'Não informado')}")
            print(f"Bairro: {dados_cep.get('bairro', 'Não informado')}")
            print(f"Cidade: {dados_cep.get('localidade', 'Não informado')}")
            print(f"Estado: {dados_cep.get('uf', 'Não informado')}")

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
    except ValueError as e:
        print(f"Erro ao decodificar JSON: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

consultar_cep()