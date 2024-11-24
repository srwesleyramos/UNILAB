n = int(input('Por favor, me informe a quantidade de números: '))

primeiro = None
segundo = None

for i in range(1, n + 1):
    if i > 2:
        j = 0

        for k in range(i, 0, -1):
            if i % k == 0:
                j += 1

        if j == 2:
            if primeiro is None:
                primeiro = i
            else:
                if i >= primeiro:
                    segundo = primeiro
                    primeiro = i
                elif i >= segundo:
                    segundo = i

print('O segundo maior número é:', segundo)