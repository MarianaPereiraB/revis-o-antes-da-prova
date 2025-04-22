#faça um algorítmo para receber um número qualquer e imrimir na tela se o número é par ou ímpar, positivo ou negativo
novo = "s"
while novo == "s" :
    numqualquer = int(input("digite um número: "))
    if numqualquer <0 and numqualquer %2 == 0:
        print(f"{numqualquer} é negativo e par")
    elif numqualquer >0 and numqualquer %2 ==0:
            print(f"{numqualquer} é positivo e par")
    elif numqualquer >0 %1 == 0:
        print(f"{numqualquer} é positivo e impar")
    elif numqualquer <0 %1 == 0:
         print(f"{numqualquer} é negativo e impar")
    novo = input("deseja realizar a verificação de um novo número? ")








