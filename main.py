from calculadora import soma,sub

# Implementação da calculadora simples
while True:

    print("------------------------ CALCULADORA ------------------------------")




#menu
    print("1. soma")
    print("2. Subtração")
    print("3. sair")


    op = int(input("Opção: "))

    if op == 1:
        print("Soma")

        v1 = int(input("Informe o valor1: "))
        v2 = int(input("Informe o outro numero: "))

        total = soma(v1,v2)

        print(f"A soma é {total}")

    elif op == 2:
        print("Subtração")

        v1 = int(input("Informe o valor1: "))
        v2 = int(input("Informe o outro numero: "))

        total = sub(v1,v2)

        print(f"A sub é {total}")
    elif op == 3:
        print("Marcha")
        break
    else:
        print("Erro: Esse número de opção não existe")
        #Tratamento de erro


