# x = input("Digite sua idade: ")
# x = int(x)
#
# texto1 = "maior de idade"
# texto2 = "menor de idade"
#
# if (x >= 18):
# 	print(texto1)
# else:
# 	print(texto2)

idade = input("Digite uma idade: ")
idade = int(idade)

if (idade >= 18):
    print("Você possui maioridade")
else:
    if (idade < 12):
        print("Você é criança")
    else:
        print("Você é adolescente")

    print("Você NÃO possui maioridade")
