class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def __repr__(self):
        return f"Animal(nombre={self.nombre}, edad={self.edad}, tipo={self.tipo})"

class Node:
    def __init__(self, animal):
        self.animal = animal
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    def es_vacio(self):
        return self.cabeza is None
    def agregar_animal(self,animal):
        nodo=Node(animal)
        if self.es_vacio():
            self.cabeza= nodo
            #NONE ES VACIO

