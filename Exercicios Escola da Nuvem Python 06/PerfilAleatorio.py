import requests

def get_random_user_profile():
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

        user = data['results'][0]
        name = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        country = user['location']['country']

        print(f"Nome: {name}")
        print(f"Email: {email}")
        print(f"País: {country}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
    except KeyError as e:
        print(f"Erro ao processar os dados da API: Chave não encontrada {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

get_random_user_profile()