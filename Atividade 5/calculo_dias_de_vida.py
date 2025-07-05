from datetime import datetime

data_nasc_str = input("Digite sua data de nascimento (formato: DD/MM/AAAA): ")

data_nascimento = datetime.strptime(data_nasc_str, "%d/%m/%Y")

hoje = datetime.today()

dias_vivo = (hoje - data_nascimento).days

print(f"Você está vivo há {dias_vivo} dias.")
