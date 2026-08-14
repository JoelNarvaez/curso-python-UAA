# Autor: Joel Narvaez
# Materia: Programcion en Python

# Fecha: 14 de agosto del 2026
# Actividad: Multiplicacion de dos variables
print("MULTIPLICACION DE DOS VARIABLES")
a = float(input("Numero 1: "))
b = float(input("Numero 2: "))
print("Multiplicacion: ", a * b, "\n")

# Fecha: 14 de agosto del 2026
# Actividad: Contar voacles usando asignacion directa
print("CONTAR VARIABLES USANDO ASIGNACION DIRECTA")
pal = input("Palabra: ").lower()
voacles = pal.count("a") + pal.count("e") + pal.count("i") + pal.count("o") + pal.count("u") + pal.count("á") + pal.count("é") + pal.count("í") + pal.count("ó") + pal.count("ú")
print("Vocales: ", voacles, "\n")


# Fecha: 14 de agosto del 2026
# Actividad: Sacar area y perimtro usando format "f"
print("AREA Y PERIMETRO DE UN RECTANGULO")
base = float(input("Numero base: "))
altura = float(input("Numero altura: "))
area = base * altura
perimetro = 2 * (base + altura)
print(f"Area: {area:.2f}")
print(f"Perimetro: {perimetro:.2f}", "\n")

# Fecha: 14 de agosto del 2026
# Actividad: Signo de un numero proporcionado
print("SIGNO DE UN NUMERO ENTERO")
entero = int(input("Numero entero: "))

if (entero > 0):
    print("El numero es POSITIVO", "\n")
elif (entero < 0):
    print("El numero es NEGATIVO", "\n")
else:
    print("El numero es 0 (CERO)", "\n")

# Fecha: 14 de agosto del 2026
# Actividad: Clasificacion de edad
print("CLASIFICACION DE EDAD")

edad = int(input("Escribe tu edad: "))

if edad < 0:
    print("No exiten las edades negativas", "\n")

if edad >= 0 and edad <= 12:
    print("Niño", "\n")
elif edad >= 13 and edad <= 17:
    print("Joven o Adolescente", "\n")
elif edad >= 18 and edad <= 64:
    print("Adulto", "\n")
else:
    print("Adulto mayor", "\n")