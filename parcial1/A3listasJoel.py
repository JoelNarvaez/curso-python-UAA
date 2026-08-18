#Autor: Joel Narvaez Martinez
#Materia: Programacion en python
#Fecha: 18 de agosto del 2026
#Actividad: aprender a manipular listas  mediante ciclos for y metodos

#Ejemplo del profesor
# productos = [
#     "Laptop","Mouse","Teclado","Monitor","Audífonos","Bocina Bluetooth",
#     "Celular","Tablet","Cargador","Cable USB","Memoria USB","Disco duro externo",
#     "SSD","Memoria RAM","Webcam","Micrófono","Impresora","Tinta para impresora",
#     "Router","Switch de red","Cámara de seguridad","Smartwatch","Control de videojuegos",
#     "Videojuego","Silla gamer","Escritorio","Mochila","Libreta","Pluma","Lápiz",
#     "Borrador","Regla","Calculadora","Carpeta","Papel",
#     "Tijeras","Pegamento","Marcadores","Pintura","Cuaderno"
# ]
#
# print("Inventario de tienda (40 productos)");
#
# for p in productos:
#     print('-', p) # aparecen productos con un guion al inicio
#
# busqueda = input("\n Buscar productos (escribe parte del nombre): ").strip().lower() #strip es como el trim()
#
# if busqueda:
#     encontrados = [p for p in productos if busqueda in p.lower()]
#     if encontrados:
#         print("\nEncontrado(s): ")
#         for p in encontrados:
#             print("-",p)
#     else:
#         print("\nNo se encotraron productos")
# else:
#     print("\nBusqueda cancelada")


#Ejercicio puesto por el profesor

misCompas = ["Mariel Villalpando","Julian Emanuel Hernandez","Ana Lorena Rosales","Wendy Valadez","Emiliano Santos","Mike Zavala","Fernanda Mejia",
            "Tania Paola Garcia","Diana Ruth Marquez","Alberto Pedroza", "Eduardo Pedroza"]

print("\n\n A continuacion una lista de compañeros")
indice = 0;

for c in misCompas:
    indice = indice + 1
    print(indice, ".-", c)

busqueda = input("\nDime con quien irias por unas cheves (puede ser solo una parte del nombre): ").strip().lower()

indice = 0;
if busqueda:
    encontrados = [p for p in misCompas if busqueda in p.lower()]
    if encontrados:
        print("\nPersonas chevecheras: ")
        for p in encontrados:
            indice = indice + 1
            print(indice,p)
        print("\nCompañeros encontreados: ", indice, "en la lista de encontrados")
    else:
        print("\nNo se encotraro gente alcoholica, intenta con otro nombre")
else:
    print("\nLa busqueda termino")
