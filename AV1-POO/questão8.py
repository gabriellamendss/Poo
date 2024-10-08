maior_acerto = 0
menor_acerto = 10
total_alunos = 0
soma_notas = 0
print("Seu gabarito (A - E)")
def calcular_nota(respostas):
    acertos = 0
    for i in range(10):
        if respostas[i].upper() == gabarito[i]:
            acertos += 1
    return acertos

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

while True:
    respostas_aluno = []
    for i in range(10):
        resposta = input(f"Questão {i + 1}: ")
        respostas_aluno.append(resposta)

    nota = calcular_nota(respostas_aluno)
    print(f"\nNota do aluno: {nota} acertos.\n")

    total_alunos += 1
    soma_notas += nota
    if nota > maior_acerto:
        maior_acerto = nota
    if nota < menor_acerto:
        menor_acerto = nota

    continuar = input("Outro aluno vai utilizar o sistema? (S/N): ").upper()
    if continuar != 'S':
        break

print("\nEstatistica da Turma")
print(f"Maior acerto: {maior_acerto}")
print(f"Menor acerto: {menor_acerto}")
print(f"Total de alunos que utilizaram o sistema: {total_alunos}")
media_turma = soma_notas / total_alunos if total_alunos > 0 else 0
print(f"Média da turma: {media_turma:.2f}")
