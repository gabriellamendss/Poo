num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

print("O número {} foi divisível {} vezes.".format(num, contador))

if contador == 2:
    print("ele é primo")
else:
    print("ele não é primo")