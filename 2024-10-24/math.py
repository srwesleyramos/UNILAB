def somar(n1, n2):
    res = n1 + n2

    print(f"\nResultado da soma é: {res}")


def subtrair(n1, n2):
    res = n1 - n2

    print(f"\nResultado da subtração é: {res}")


def multiplicar(n1, n2):
    res = n1 * n2

    print(f"\nResultado da multiplicação é: {res}")


def dividir(n1, n2):
    res = n1 / n2

    print(f"\nResultado da divisão é: {res}")


while True:
    print("   MENU CALCULADORA")
    print()
    print("Escolha a opção desejada:")
    print(" 1. Somar")
    print(" 2. Subtrair")
    print(" 3. Multiplicar")
    print(" 4. Dividir")
    print()

    o = input(" >> ")

    x = int(input("\nEscolha o primeiro número: "))
    y = int(input("Escolha o segundo número: "))

    if o == "1":
        somar(x, y)
    elif o == "2":
        subtrair(x, y)
    elif o == "3":
        multiplicar(x, y)
    elif o == "4":
        dividir(x, y)
    else:
        print("Opção inválida!")
