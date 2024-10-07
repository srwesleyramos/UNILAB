p = float(input("Qual % de presença nas aulas? "))
n1 = float(input("Qual a primeira nota? "))
n2 = float(input("Qual a segunda nota? "))
t = float(input("Qual a nota do trabalho? "))

ms = (n1 + n2) / 2
mp = (ms * 60 + t * 40) / 100

if mp >= 6 and p >= 75:
	print("Você foi aprovado!")
else:
	print("Você foi reprovado!")