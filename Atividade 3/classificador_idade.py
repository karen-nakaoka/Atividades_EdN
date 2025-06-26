idade = int(input("Qual é a sua idade? "))

if idade >= 0 and idade < 13:
    classificacao = "criança"
elif idade >= 13 and idade < 18:
    classificacao = "adolescente"
elif idade >= 18 and idade < 60:
    classificacao = "adulto"
elif idade >= 60:
    classificacao = "idoso"
else:
    classificacao = "Idade Inválida"

print(f"Você tem {idade} anos e é {classificacao}.")
