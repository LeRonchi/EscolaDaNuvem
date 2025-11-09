import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = int(input("Digite o comprimento desejado para a senha: "))

if password_length <= 0:
    print("O comprimento da senha deve ser um número positivo.")
else:
    random_password = generate_password(password_length)
    print(f"Sua senha aleatória é: {random_password}")