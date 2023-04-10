print("Bem-vindo(a) ao calculador de IMC!")

peso = float(input("Por favor, informe o seu peso em quilogramas (kg): "))
altura = float(input("Agora, informe a sua altura em metros (m): "))


imc = peso / altura**2

print("O seu IMC é: {:.2f}".format(imc))
