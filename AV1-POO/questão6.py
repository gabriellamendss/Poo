def calcular_salario():
    salario_inicial = 1000.00
    aumento_1996 = 0.015

    salario = salario_inicial
    salario += salario * aumento_1996
    aumento_anual = aumento_1996 * 2
    for ano in range(1997, 2026):
        salario += salario * aumento_anual
        aumento_anual *= 2
    return salario
salario_2025 = calcular_salario()
print(f"O salário do funcionário em 2025 será: R$ {salario_2025:.2f}")
