def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

conta = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))

valor_gorjeta = calcular_gorjeta(conta, porcentagem)

print(f"A gorjeta a ser deixada é: R$ {valor_gorjeta:.2f}")