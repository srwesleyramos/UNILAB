import random

x = random.randint(1, 10)

while True:
    y = random.randint(1, 10)

    if y != x:
        break

while True:
    z = random.randint(1, 10)

    if z != x and z != y:
        break

print(x, y, z)