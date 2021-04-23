class PerCent:
    def Acréscimo_Percentual():
        i = 1
        while(i>0):
            num = float(input("Digite um número qualquer: "))
            P = float(input("Digite o valor Acréscimo/Descrécimo percentual: "))
            R = num + (num * P) / 100

            print("")
            print("Resultado: %.2f" % R)

            print("")
            print("")
            print("Digite 1 para continuar ou 0 para sair: ")
            i = int(input())


    def Valor_Percentual():
        i = 1
        while (i > 0):
            num1 = float(input("Digite o 1º/2º número: "))
            num2 = float(input("Digite o 2º/2º número: "))
            R = (num1 / num2) * 100

            print("")
            print("Resultado: %.2f" % R , "%")

            print("")
            print("")
            print("Digite 1 para continuar ou 0 para sair: ")
            i = int(input())

    def Valor_Numérico():
        i = 1
        while (i > 0):
            num = float(input("Digite um número: "))
            P = float(input("Digite um valor percentual: "))
            R = (num * P) / 100

            print("")
            print("Resultado: %.2f" % R)

            print("")
            print("")
            print("Digite 1 para continuar ou 0 para sair: ")
            i = int(input())

a = PerCent
print("Digite 1 para fazer Acréscimo/Descrécimo percentual: ")
print("Digite 2 para descobrir o valor percentual: ")
print("Digite 3 para descobrir o valor do número de acordo com a percentagem : ")
op = int(input())
if (op==1):
    a.Acréscimo_Percentual()
if (op==2):
    a.Valor_Percentual()
if (op==3):
    a.Valor_Numérico()


input()

