# Autor: Joel Narvaez Martinez
# Materia: Programacion en python
# Fecha: 8/12/2026
# Actividad: La actividad consite en practicar
#             los conceptos fundamentales de python
#             como introduccion al lenguaje

#Operadores aritmeticos

print("EJERCICIO DE LA PRESENTACION")
5 + 6
10 % 3
5 ** 3
9 // 2

#Variables
nombre = 5
type(nombre)
nombre = "Juan"
type(nombre)
nombre = 5.2

#Cadenas de texto e impresion
mensaje = """Este es un mensaje 
... con tres saltos
... de linea"""
print(mensaje)


numero1 = 5
numero2  = 7

#Condicional if con su respectivo else
if numero1>numero2:
    print("El numero 1 es mayor", "\n")
else:
    print("El numero 2 es amyor",  "\n")


# Fecha: 13 de agosto del 2026
# Actividad: Manejar input, realizar una suma
print('SUMA')

a = float(input("Numero 1: "))
b = float(input("Numero 2: "))

print("Suma: ", a+b, "\n");

# Fecha: 13 de agosto del 2026
# Actividad: Leer dos valores y cambiarlos usando una variable temporal
print("VARIABLE TEMPORAL")

x = input("x: ")
y = input("y: ")

temp = x
x = y
y = temp

print("X=", x, "Y=", y, "\n")

# Fecha: 13 de agosto del 2026
# Actividad: Pedir una palabra, muestra su longitud y version en mayusculas
print("EJERCICIO PALABRA, LENGITUD Y A MAYUSCULAS")

pal = input("Palabra: ")
print("Largo: ", len(pal))
print("Mayusculas", pal.upper(), "\n") #.upper es un metodo para convertir la palabra en mayusculas

# Fecha: 13 de agosto del 2026
# Actividad: Calcualr el promedio de 3 numero (Mostrar solo dos decimales)
print("PROMEDIO")

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))

prom = (n1+n2+n3)/3
print(f"El promedio es: {prom:.2f}", "\n") # con .2f especificamos cuantos decimales queremos

# Fecha: 14 de agosto del 2026
# Actividad: Pedir un numero entero y decir si es par o impar
print("PAR O IMPAR")

n = int(input("Entero: "))
if n % 2 == 0:
    print("Par", "\n")
else:
    print("Impar", "\n")
