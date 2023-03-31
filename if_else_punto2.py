# Solicitar al usuario las notas de las materias
desarrollo_de_software = float(input("Ingrese la nota de Desarrollo de Software: "))
matematicas = float(input("Ingrese la nota de Matemáticas: "))
logica_programacion = float(input("Ingrese la nota de Lógica de Programación: "))

# Calcular el promedio de las notas
promedio = (desarrollo_de_software + matematicas + logica_programacion) / 3

# Determinar si el estudiante aprobó o no
if promedio >= 3.0:
    print("Aprobado")
else:
    print("Reprobado")
