def verificar_palindromo(texto: str) -> str:

    texto_limpo = "".join(char for char in texto.lower() if char.isalpha())
    
    texto_invertido = texto_limpo[::-1]
    
    if texto_limpo == texto_invertido:
        return "Sim"
    else:
        return "Não"

print(f"Exemplo 1 'Ovo': {verificar_palindromo('Ovo')}")

print(f"Exemplo 2'Ame a ema': {verificar_palindromo('Ame a ema')}")

print(f"Exemplo 3'Anotaram a data da maratona.': {verificar_palindromo('Anotaram a data da maratona.')}")

print(f"Exemplo 4'Socorram-me, subi no ônibus em Marrocos!': {verificar_palindromo('Socorram-me, subi no ônibus em Marrocos!')}")

print(f"Exemplo 5'Isto não é um palíndromo': {verificar_palindromo('Isto não é um palíndromo')}")

palindromo = str(input("Digite uma frase para verificar se é um palíndromo: "))
resultado = verificar_palindromo(palindromo)    
print(f"A frase digitada é um palíndromo? {resultado}")