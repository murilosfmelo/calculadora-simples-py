from calculadora import soma,sub,mul,div

# Implementação da calculadora simples
while True:

    print("------------------------ CALCULADORA ------------------------------")




#menu
    print("1. soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. sair")


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
        print("Multiplicação")

        v1 = int(input("Informe o valor1: "))
        v2 = int(input("Informe o outro numero: "))

        total = mul(v1, v2)

        print(f"A Multiplicação é {total}")
    elif op == 4:
        print("Divisão")

        v1 = int(input("Informe o valor1: "))
        v2 = int(input("Informe o outro numero: "))

        total = div(v1, v2)
        if v1 == 0 and v2 == 0 or v2 == 0 and v1 == 0:
            print("Divisão de 0 é 0")
        else:
            print(f"A Divisão é {total}")
    elif op == 5:
        print("Marcha")
        break
    else:
        print("Erro: Esse número de opção não existe")
        #Tratamento de erro feito


