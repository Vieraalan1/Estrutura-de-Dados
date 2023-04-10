alunos = {}

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

soma = 0
for nota in alunos.values():
    soma += nota
media = soma / len(alunos)

print(f"A média das notas é {media:.2f}")
