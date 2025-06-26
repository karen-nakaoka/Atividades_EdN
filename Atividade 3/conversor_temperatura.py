unidade_origem = int(input("Qual é a unidade de origem?\n1. Celsius\n2. Fahrenheit\n3. Kelvin\n"))
unidade_final = int(input("Para qual unidade deseja converter?\n1. Celsius\n2. Fahrenheit\n3. Kelvin\n"))
temperatura_inicial = float(input("Qual é a temperatura a ser convertida? "))

if unidade_origem == 1 and unidade_final == 2:
    temperatura_final = (temperatura_inicial * 9/5) + 32
    simbolo_origem = "ºC"
    simbolo_final = "ºF"
elif unidade_origem == 1 and unidade_final == 3:
    temperatura_final = temperatura_inicial + 273.15
    simbolo_origem = "ºC"
    simbolo_final = "K"
elif unidade_origem == 2 and unidade_final == 1:
    temperatura_final = (temperatura_inicial - 32) * 5/9
    simbolo_origem = "ºF"
    simbolo_final = "ºC"
elif unidade_origem == 2 and unidade_final == 3:
    temperatura_final = (temperatura_inicial - 32) * 5/9 + 273.15
    simbolo_origem = "ºF"
    simbolo_final = "K"
elif unidade_origem == 3 and unidade_final == 1:
    temperatura_final = temperatura_inicial - 273.15
    simbolo_origem = "K"
    simbolo_final = "ºC"
elif unidade_origem == 3 and unidade_final == 2:
    temperatura_final = (temperatura_inicial - 273.15) * 9/5 + 32
    simbolo_origem = "K"
    simbolo_final = "ºF"
elif unidade_origem == unidade_final:
    temperatura_final = temperatura_inicial
    if unidade_origem == 1:
        simbolo_origem = simbolo_final = "ºC"
    elif unidade_origem == 2:
        simbolo_origem = simbolo_final = "ºF"
    elif unidade_origem == 3:
        simbolo_origem = simbolo_final = "K"
    print("Você escolheu a mesma unidade para origem e destino.")
else:
    print("Opção inválida.")
    exit()

print(f"\nTemperatura inicial: {temperatura_inicial:.2f} {simbolo_origem}")
print(f"Temperatura convertida: {temperatura_final:.2f} {simbolo_final}")