n = int(input('Por favor, me informe o intervalo: '))

cinco = 0
tres = 0

for i in range(0, n):
    if i % 3 == 0:
        tres += 1

    if i % 5 == 0:
        cinco += 1

print('Divisíveis por tres:', tres)
print('Divisíveis por cinco:', cinco)