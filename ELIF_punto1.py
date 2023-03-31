# Solicitando al usuario que ingrese los cuatro números
num1 = int(input("Ingrese el primer número:"))
num2 = int(input("Ingrese el segundo número:"))
num3 = int(input("Ingrese el tercer número:"))
num4 = int(input("Ingrese el cuarto número:"))

# Comprobando si algún número aparece dos veces
if num1 == num2 or num1 == num3 or num1 == num4 or num2 == num3 or num2 == num4 or num3 == num4:
    print("Al menos un número se repite dos veces.")
else:
    # Comprobando si todos los números son iguales
    if num1 == num2 == num3 == num4:
        print("Todos los números son iguales.")
    else:
        # Comprobando si todos los números son diferentes
        if num1 != num2 and num1 != num3 and num1 != num4 and num2 != num3 and num2 != num4 and num3 != num4:
            print("Todos los números son diferentes.")
