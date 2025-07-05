def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return round(preco_final, 2), round(desconto, 2)

preco = float(input("Digite o preço do produto (R$): "))
percentual = float(input("Digite a porcentagem de desconto (%): "))

preco_com_desconto, valor_do_desconto = calcular_desconto(preco, percentual)

print(f"\nDesconto aplicado: R$ {valor_do_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_com_desconto:.2f}")