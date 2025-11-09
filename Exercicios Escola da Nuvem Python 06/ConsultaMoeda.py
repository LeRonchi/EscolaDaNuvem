import requests

def consultar_cotacao_moeda():
    moeda_desejada = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ").upper()
    
    if not moeda_desejada.isalpha() or len(moeda_desejada) != 3:
        print("Código de moeda inválido. Por favor, digite um código de 3 letras (ex: USD).")
        return
    
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_desejada}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status() 
        dados_cotacao = response.json()

        
        chave_moeda = moeda_desejada + "BRL"
        if chave_moeda in dados_cotacao:
            cotacao = dados_cotacao[chave_moeda]
            
            nome_moeda = cotacao.get('name', 'Não disponível')
            valor_atual = cotacao.get('bid', 'Não disponível') 
            valor_maximo = cotacao.get('high', 'Não disponível')
            valor_minimo = cotacao.get('low', 'Não disponível')
            timestamp = int(cotacao.get('timestamp', 0))
            
            from datetime import datetime
            data_atualizacao = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

            print(f"\nCotação de {nome_moeda}:")
            print(f"Valor Atual (Compra): R$ {valor_atual}")
            print(f"Valor Máximo (24h): R$ {valor_maximo}")
            print(f"Valor Mínimo (24h): R$ {valor_minimo}")
            print(f"Última atualização: {data_atualizacao}")
        else:
            print(f"Não foi possível encontrar dados de cotação para {moeda_desejada}-BRL. Verifique o código da moeda.")

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão com a API: {e}")
    except ValueError as e:
        print(f"Erro ao decodificar JSON: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

consultar_cotacao_moeda()