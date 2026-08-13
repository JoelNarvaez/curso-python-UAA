# Autor: Joel Narvaez
# Materia: Programcion en Python
# Fecha: 13 de agosto del 2026
# Actividad: Manejar input, realizar una suma

print('SUMA')

a = float(input("Numero 1: "))
b = float(input("Numero 2: "))

print("Suma: ", a+b);

# Autor: Joel Narvaez
# Materia: Programcion en Python
# Fecha: 13 de agosto del 2026
# Actividad: Leer dos valores y cambiarlos usando una variable temporal

print("VARIABLE TEMPORAL")

x = input("x: ")
y = input("y: ")

temp = x
x = y
y = temp

print("X=", x, "Y=", y)

# Autor: Joel Narvaez
# Materia: Programcion en Python
# Fecha: 13 de agosto del 2026
# Actividad: Pedir una palabra, muestra su longitud y version en mayusculas

print("EJERCICIO PALABRA, LENGITUD Y A MAYUSCULAS")

pal = input("Palabra: ")
print("Largo: ", len(pal))
print("Mayusculas", pal.upper()) #.upper es un metodo para convertir la palabra en mayusculas


# Autor: Joel Narvaez
# Materia: Programcion en Python
# Fecha: 13 de agosto del 2026
# Actividad: Calcualr el promedio de 3 numero (Mostrar solo dos decimales)

print("PROMEDIO")

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))

prom = (n1+n2+n3)/3
print(f"El promedio es: {prom:.2f}") # con .2f especificamos cuantos decimales queremos
