notas = []

quantidade_alunos = int(input("Quantos alunos há na turma? "))

for i in range(quantidade_alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

soma = sum(notas)
media = soma / quantidade_alunos

print(f"\nA média da turma é: {media:.2f}")
