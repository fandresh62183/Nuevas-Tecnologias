# Mostrar el menú de opciones de colores primarios
print("Seleccione dos colores primarios:")
print("1. Amarillo")
print("2. Azul")
print("3. Rojo")
print("4. Blanco")
print("5. Negro")

# Solicitar al usuario que ingrese sus opciones
opcion1 = int(input("Elija el primer color (ingrese el número correspondiente): "))
opcion2 = int(input("Elija el segundo color (ingrese el número correspondiente): "))

# Evaluar las posibles combinaciones
if opcion1 == 1 and opcion2 == 2 or opcion1 == 2 and opcion2 == 1:
    print("La combinación de amarillo y azul genera verde.")
elif opcion1 == 1 and opcion2 == 3 or opcion1 == 3 and opcion2 == 1:
    print("La combinación de amarillo y rojo genera naranja.")
elif opcion1 == 1 and opcion2 == 4 or opcion1 == 4 and opcion2 == 1:
    print("La combinación de amarillo y blanco no genera otro color primario.")
elif opcion1 == 1 and opcion2 == 5 or opcion1 == 5 and opcion2 == 1:
    print("La combinación de amarillo y negro no genera otro color primario.")
elif opcion1 == 2 and opcion2 == 3 or opcion1 == 3 and opcion2 == 2:
    print("La combinación de azul y rojo genera violeta.")
elif opcion1 == 2 and opcion2 == 4 or opcion1 == 4 and opcion2 == 2:
    print("La combinación de azul y blanco no genera otro color primario.")
elif opcion1 == 2 and opcion2 == 5 or opcion1 == 5 and opcion2 == 2:
    print("La combinación de azul y negro no genera otro color primario.")
elif opcion1 == 3 and opcion2 == 4 or opcion1 == 4 and opcion2 == 3:
    print("La combinación de rojo y blanco no genera otro color primario.")
elif opcion1 == 3 and opcion2 == 5 or opcion1 == 5 and opcion2 == 3:
    print("La combinación de rojo y negro no genera otro color primario.")
elif opcion1 == 4 and opcion2 == 5 or opcion1 == 5 and opcion2 == 4:
    print("La combinación de blanco y negro no genera otro color primario.")
else:
    print("Opciones no válidas.")
