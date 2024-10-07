aluno = input('Informe o nome do aluno: ')
media = float(input('Informe a sua média final: '))

if media >= 6:
    print("O aluno", aluno, "foi aprovado!")
else:
    print("O aluno", aluno, "foi para a recuperação.")

    rec = float(input("Informe a nota final: "))

    if rec >= 5:
       print("O aluno", aluno, "foi aprovado!")
    else:
        print("O aluno", aluno, "foi reprovado!")
