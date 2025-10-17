def cuenta_regresiva (n):
    if n == 0: #caso base
        print("¡Despegue o Salida!")
    else:
        print(f"{n}......")
        cuenta_regresiva (n-1)

# Programa Pricipal
num = int(input("Ingrese el numero para realizar la cuenta regresiva con recursividad"))
cuenta_regresiva (num)        