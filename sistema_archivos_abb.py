


class Nodo:
    def __init__(self, nombre, extension, tamano, tipo):
        self.nombre = nombre         
        self.extension = extension    
        self.tamano = tamano          
        self.tipo = tipo             
        self.izquierdo = None         
        self.derecho = None           

    
    def mostrar(self):
        print("Nombre:", self.nombre, "| Extensión:", self.extension,
              "| Tamaño:", self.tamano, "bytes | Tipo:", self.tipo)


class Arbol:
    def __init__(self, nombre_raiz):
        
        self.raiz = Nodo(nombre_raiz, "-", 0, "Directorio")

    
    def insertar(self, actual, nuevo):
        clave_nueva = nuevo.nombre.lower()
        clave_actual = actual.nombre.lower()

        
        if clave_nueva == clave_actual:
            print("ERROR: El elemento '" + nuevo.nombre + "' ya existe.")
            return False

       
        if actual.tipo == "Archivo":
            print("ERROR: No se puede insertar el elemento.")
            print("Un archivo no puede contener otros elementos.")
            return False

        if clave_nueva < clave_actual:
            if actual.izquierdo is None:
                actual.izquierdo = nuevo
                return True
            return self.insertar(actual.izquierdo, nuevo)
        else:
            if actual.derecho is None:
                actual.derecho = nuevo
                return True
            return self.insertar(actual.derecho, nuevo)

    
    def buscar(self, actual, nombre):
        if actual is None:
            return None
        clave_buscada = nombre.lower()
        clave_actual = actual.nombre.lower()
        if clave_buscada == clave_actual:
            return actual
        if clave_buscada < clave_actual:
            return self.buscar(actual.izquierdo, nombre)
        else:
            return self.buscar(actual.derecho, nombre)

    
    def inorden(self, actual):
        if actual is not None:
            self.inorden(actual.izquierdo)
            actual.mostrar()
            self.inorden(actual.derecho)

    
    def preorden(self, actual):
        if actual is not None:
            actual.mostrar()
            self.preorden(actual.izquierdo)
            self.preorden(actual.derecho)

    
    def postorden(self, actual):
        if actual is not None:
            self.postorden(actual.izquierdo)
            self.postorden(actual.derecho)
            actual.mostrar()



def validar_datos(nombre, extension, tamano, tipo):
    if nombre == "":
        print("ERROR: El nombre no puede estar vacío.")
        return False
    if tipo == "Directorio" and "." in nombre:
        print("ERROR: Un directorio no puede tener extensión.")
        return False
    if tipo == "Archivo" and extension == "":
        print("ERROR: Un archivo debe tener extensión.")
        return False
    if tamano < 0:
        print("ERROR: El tamaño debe ser un número entero mayor o igual a 0.")
        return False
    return True



def pedir_tamano():
    texto = input("Tamaño en bytes: ").strip()
    if texto.isdigit():
        return int(texto)
    return -1




def crear_directorio(arbol):
    nombre = input("Nombre del directorio: ").strip()
    if validar_datos(nombre, "-", 0, "Directorio"):
        nuevo = Nodo(nombre, "-", 0, "Directorio")
        if arbol.insertar(arbol.raiz, nuevo):
            print("Directorio creado correctamente.")


def insertar_archivo(arbol):
    nombre = input("Nombre del archivo (sin extensión): ").strip()
    extension = input("Extensión (ejemplo: txt): ").strip()
    tamano = pedir_tamano()
    if validar_datos(nombre, extension, tamano, "Archivo"):
        nuevo = Nodo(nombre, extension, tamano, "Archivo")
        if arbol.insertar(arbol.raiz, nuevo):
            print("Archivo insertado correctamente.")


def buscar_elemento(arbol):
    nombre = input("Nombre a buscar: ").strip()
    nodo = arbol.buscar(arbol.raiz, nombre)
    if nodo is None:
        print("El elemento no existe en el sistema de archivos.")
    else:
        print("Elemento encontrado")
        print("Nombre:", nodo.nombre)
        print("Extensión:", nodo.extension)
        print("Tipo:", nodo.tipo)
        print("Tamaño:", nodo.tamano, "bytes")


def mostrar_recorrido(arbol):
    print("1. Inorden")
    print("2. Preorden")
    print("3. Postorden")
    opcion = input("Elige el recorrido: ").strip()
    if opcion == "1":
        print("--- Recorrido inorden ---")
        arbol.inorden(arbol.raiz)
    elif opcion == "2":
        print("--- Recorrido preorden ---")
        arbol.preorden(arbol.raiz)
    elif opcion == "3":
        print("--- Recorrido postorden ---")
        arbol.postorden(arbol.raiz)
    else:
        print("Opción no válida.")




def menu():
    print("=== SISTEMA DE ARCHIVOS CON ABB ===")
    
    nombre_raiz = input("Nombre del directorio raíz: ").strip()
    while not validar_datos(nombre_raiz, "-", 0, "Directorio"):
        nombre_raiz = input("Nombre del directorio raíz: ").strip()
    arbol = Arbol(nombre_raiz)
    print("Directorio raíz '" + nombre_raiz + "' creado.")

    opcion = ""
    while opcion != "5":
        print()
        print("----- MENÚ -----")
        print("1. Crear directorio")
        print("2. Insertar archivo")
        print("3. Buscar elemento por nombre")
        print("4. Mostrar recorrido")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            crear_directorio(arbol)
        elif opcion == "2":
            insertar_archivo(arbol)
        elif opcion == "3":
            buscar_elemento(arbol)
        elif opcion == "4":
            mostrar_recorrido(arbol)
        elif opcion == "5":
            print("Saliendo del programa.")
        else:
            print("Opción no válida.")


menu()
