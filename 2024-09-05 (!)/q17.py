numero = int(input("Informe um número: "))
primo = True

index = numero - 1

while (index > 1):
    if (numero % index == 0):
        primo = False
        break
    index -= 1

if (primo):
    print("O número é primo!")
else:
    print("O número não é primo!")