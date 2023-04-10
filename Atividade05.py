numeros = []

for i in range(5):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

soma = 0

for num in numeros:
    soma += num

print("A soma dos números digitados é:", soma)
