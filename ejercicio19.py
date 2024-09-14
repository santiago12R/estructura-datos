class Animal:

        def __init__(self,nombre, edad,tipo):
                
                self.nombre = nombre
                self.edad = edad
                self.tipo = tipo

class Node:

        def  __init__(self,animal):

            self.animal=animal
            self.next=None      

class ListaEnlazada:

    def __init__(self) :

        self.cabeza= None

    def es_vacio(self):
        return self.cabeza is None
        
    def agregar_animal(self, animal):
        Nodo =Node(animal)
        if self.es_vacio():
              self.cabeza= Nodo
        else:
            nodo_actual = self.cabeza
    def mostrar_animalesbucle(self):
        actual = self.cabeza
        while nodo_actual.next is not None:
                 nodo_actual = nodo_actual.next
        nodo_actual.next = Node

    def mostrar_animales_recursivo(self, nodo):
        if nodo is None:
            return
        print(nodo.animal)
        self.mostrar_animales_recursivo(nodo.next)
    

         
   
         
              


                      