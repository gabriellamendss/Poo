pares = 0
impares = 0
# range do loop
print('Insira 10 numeros para a contagem')
for i in range(10):
      numero = int(input(f"{i + 1}º número inteiro: "))
      if numero % 2 == 0:
            pares += 1
      else:
            impares += 1

print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
