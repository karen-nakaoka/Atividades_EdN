peso = float(input("Qual é o seu peso?(em kg) "))
altura = float(input("Qual é a sua altura? (em metros) "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc >= 18.5 and imc < 25:
    classificacao = "Peso normal"
elif imc >= 25 and imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"Seu IMC é {imc:.1f} e sua classificação é: {classificacao}")