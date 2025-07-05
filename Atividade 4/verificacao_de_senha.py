senha = input("Olá! Digite sua nova senha: ")

tem_tamanho_minimo = len(senha) >= 8
tem_numero = any(caractere.isdigit() for caractere in senha)

if tem_tamanho_minimo and tem_numero:
    print("Senha válida!")
else:
    print("Senha inválida. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")