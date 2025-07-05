pares = 0
impares = 0

print("Digite os números que deseja analisar.")
print("Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")

    if entrada.lower() == 'sair':
        break

    if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
        numero = int(entrada)

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'sair'.")

print("\nAnálise concluída!")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
