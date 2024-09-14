year = int(input("Me informe seu ano de nascimento: "))
month = int(input("Me informe seu mês de nascimento: "))
day = int(input("Me informe seu dia de nascimento: "))

CURRENT_YEAR = 2024
CURRENT_MONTH = 8
CURRENT_DAY = 29

if (CURRENT_MONTH > month) or (CURRENT_MONTH == month and CURRENT_DAY >= day):
	print("Sua idade, é:", CURRENT_YEAR - year)
else:
	print("Sua idade, é:", CURRENT_YEAR - year - 1)