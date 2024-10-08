popA = 80000
popB = 200000
taxaA = 0.03
taxaB = 0.015
anos = 0

while popA < popB:
    popA += popA * taxaA
    popB += popB * taxaB
    anos += 1
print(f"Vai levar {anos} anos para que a população do país 'A' ultrapasse ou iguale a população do pais 'B'")