nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = (preco_original / 100) * porcentagem_desconto
preco_final = preco_original - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")

