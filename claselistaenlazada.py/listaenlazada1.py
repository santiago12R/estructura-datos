# Clase Animal
class Animal:
    def __init__(self, tipo, edad):
        self.tipo = tipo  # Tipo de animal (ej. "Águila")
        self.edad = edad  # Edad del animal

# Nodo de la lista enlazada
class Nodo:
    def __init__(self, animal):
        self.animal = animal  # El objeto Animal
        self.siguiente = None  # El siguiente nodo en la lista

# Clase ListaEnlazada para manejar los nodos
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # La lista empieza vacía

    # Método para agregar un animal a la lista, si no está repetido
    def agregar(self, animal):
        # Si la lista está vacía, agrega el primer animal
        if self.cabeza is None:
            self.cabeza = Nodo(animal)
            print(f"{animal.tipo} ha sido agregado a la lista.")
            return
        
        # Si no está vacía, recorremos la lista
        actual = self.cabeza
        while actual is not None:
            # Verificamos si el animal ya está en la lista
            if actual.animal.tipo == animal.tipo:
                print(f"{animal.tipo} ya está en la lista, no se agregará.")
                return
            if actual.siguiente is None:
                break
            actual = actual.siguiente
        
        # Agregar el nuevo animal al final de la lista
        actual.siguiente = Nodo(animal)
        print(f"{animal.tipo} ha sido agregado a la lista.")

    # Mostrar la lista de animales usando un bucle
    def mostrar_con_bucle(self):
        actual = self.cabeza
        while actual is not None:
            print(f"Animal: {actual.animal.tipo}, Edad: {actual.animal.edad}")
            actual = actual.siguiente

    # Mostrar la lista de animales usando recursión
    def mostrar_con_recursion(self, nodo):
        if nodo is None:
            return
        print(f"Animal: {nodo.animal.tipo}, Edad: {nodo.animal.edad}")
        self.mostrar_con_recursion(nodo.siguiente)
