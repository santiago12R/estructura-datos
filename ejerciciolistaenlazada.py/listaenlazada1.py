# Clase Animal
class Animal:
    def __init__(self, tipo, edad ):
        self.tipo = tipo  
        self.edad = edad  

class Nodo:
    def __init__(self, animal):
        self.animal = animal  
        self.siguiente =None
        


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
          

   
    def agregar(self, animal):
     
        if self.cabeza is None:
            
            self.cabeza = Nodo(animal)
            print(f"{animal.tipo} ha sido agregado a la lista.")
            return
        
      
        actual = self.cabeza
        while actual is not None:
        
          
            if actual.animal.tipo == animal.tipo:
                print(f"{animal.tipo} ya está en la lista, no se agregará.")
                return
            if actual.siguiente is None:
            
                break
            actual = actual.siguiente
        
        
        actual.siguiente = Nodo(animal)
        print(f"{animal.tipo} ha sido agregado a la lista.")

   
    def mostrar_con_bucle(self):
        actual = self.cabeza
        while actual is not None :
        
            print(f"Animal: {actual.animal.tipo}, Edad: {actual.animal.edad}")
            actual = actual.siguiente

   
    def mostrar_con_recursion(self, nodo):
        if nodo is None:
        
            return
        print(f"Animal: {nodo.animal.tipo}, Edad: {nodo.animal.edad}")
        self.mostrar_con_recursion(nodo.siguiente)

def agregar_animales_a_lista():
    zoologico = ListaEnlazada() 

    while True:
        tipo = input("Ingrese el tipo de animal (o 'salir' para terminar): ")
        if tipo.lower() == 'salir':
            break 

        edad = input("Ingrese la edad del animal: ")
        

        animal = Animal(tipo, edad)  
        zoologico.agregar(animal)

    return zoologico 


zoologico = agregar_animales_a_lista()


print("Mostrando animales con un bucle:")
zoologico.mostrar_con_bucle()


print("Mostrando animales con recursión:")
zoologico.mostrar_con_recursion(zoologico.cabeza)