print("***************Calculadora***************")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

try:
    operacao = int(input("Qual operação você quer fazer (1,2,3,4)? "))
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if operacao == 1:
        resultado = n1 + n2
    elif operacao == 2:
        resultado = n1 - n2
    elif operacao == 3:
        resultado = n1 * n2
    elif operacao == 4:
        if n2 == 0:
            resultado = "Erro: divisão por zero"
        else:
            resultado = n1 / n2
    else:
        resultado = "Operação inválida"

except ValueError:
    resultado = "Entrada inválida. Por favor, digite números."

print("Resultado = ", resultado)