
n = int(input("Digite o número de alunos: "))


notas = []


for _ in range(n):
    nota = float(input())
    notas.append(nota)


media = sum(notas) / n


limite_acima = media * 1.1
limite_abaixo = media * 0.9


acima = sum(1 for nota in notas if nota > limite_acima)


abaixo = sum(1 for nota in notas if nota < limite_abaixo)


print(f"{media:.2f}")
print(acima)
print(abaixo)