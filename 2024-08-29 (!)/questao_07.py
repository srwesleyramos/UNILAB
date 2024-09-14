renda = float(input('Por favor, informe sua renda: '))

if (renda <= 2000):
    print("Isento")
elif (renda <= 5000):
    print(renda * 0.1)
else:
    print(renda * 0.2)