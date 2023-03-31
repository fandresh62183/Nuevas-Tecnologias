# Solicitar al usuario un número
num = int(input("Ingrese un número: "))

# Verificar si el número es impar
if num % 2 != 0:
    print("El número es impar.")
else:
    print("El número no es impar.")

# Verificar si el número es primo
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("El número no es primo.")
            break
    else:
        print("El número es primo.")
else:
    print("El número no es primo.")
