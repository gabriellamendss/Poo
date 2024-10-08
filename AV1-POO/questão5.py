i = int(input('Quantas caixas o cliete esta levando (1-50): '))
preco = i * 1.99
print(f'Total: {preco}')

print("\nTabela de preços")
for i in range(1, 51):
    preco = i * 1.99
    print(f"{i} - R$ {preco:.2f}")
