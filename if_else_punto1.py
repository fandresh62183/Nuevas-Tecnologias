# Solicitar al usuario su edad y sus ingresos mensuales
edad = int(input("Ingresar edad:"))
salario = int(input("Ingresar Salario:"))

# Verificar si el usuario debe tributar o no
if edad > 18 and salario >= 2500000:
    print("Tiene que tributar")
else:
    print("No tiene que tributar")