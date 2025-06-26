valor_real = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_real / taxa_dolar
valor_euro = valor_real / taxa_euro

print(f"Valor em real: R$ {valor_real:.2f}")
print(f"Valor em dólar: $ {valor_dolar:.2f}")
print(f"Valor em euro: € {valor_euro:.2f}")