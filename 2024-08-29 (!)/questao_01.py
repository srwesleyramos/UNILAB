x = int(input("Por favor, informe sua idade: "))

if (x >= 18):
	print("Você é maior de idade")
else:
	print("Você não é maior de idade")

if (x >= 16):
	print("Você está apto para votar")
else:
	print("Você estará apto para votar em", 16-x, "ano(s)")