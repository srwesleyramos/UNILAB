primeiro = None
segundo = 0

for i in range(0,5):
    j = int(input('Por favor, me informe um número: '))

    if primeiro is None:
        primeiro = j
    else:
        if j >= primeiro:
            segundo = primeiro
            primeiro = j
        elif j >= segundo:
            segundo = j

print('O segundo maior número foi:', segundo)