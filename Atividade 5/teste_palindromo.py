import string

def eh_palindromo(texto):
    texto_limpo = ''.join(letra.lower() for letra in texto if letra.isalnum())
    
    if texto_limpo == texto_limpo[::-1]:
        return "Sim, é um palíndromo."
    else:
        return "Não, não é um palíndromo."

frase = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(frase)
print(resultado)