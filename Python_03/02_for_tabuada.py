# tabuada

while True:
    print("")
    num = int(input("informe um número: "))
    print("")
    print(f"Tabuada do {num} ")
    print(" ")

    # gerar Tabuada usando laço for

    for i in range (1, 11):
        result = num * i
        print(f"{num} * {i} = {result} ")
        i += 1

    # pergunta se quer continuar
        continuar = input ("\nDeseja calcular outra tabuada (s/n): ?")
        if continuar.lower() != 's':
            print("Encerrando o programa.")
            break