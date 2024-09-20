class Tarea:
    def __init__(self, descripcion:str, prioridad:int, fecha_vencimiento:int,tarea:str):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento  
        self.tarea= tarea

        def __str__(self):

            return f"{self.tarea} tiene prioridad{self.prioridad}y la fecha de vencimiento es{self.fecha_vencimiento}"    
        
class Node:
    def __init__(self,tarea) :
        self.tarea = tarea
        self.next = None

class ListaDeTareas:
    def __init__(self) :
        self.cabeza = None
    
    def es_vacio(self):
        return self.cabeza is None
    
    def agregar_tarea(self,tarea):
         
         nueva_tarea = Node(tarea)

        if self.cabeza is None:
            self.cabeza = nueva_tarea
            
            print(f"{tarea.tarea} ha sido agregado tarea a la lista.")

                return
        actual = self.cabeza
       
    while actual is not None:
    
            if actual.tarea.tipo == tarea.tarea:
                print(f"{tarea.tarea} ya está en la lista, no se agregará.")
                return
            if actual.siguiente is None:
            
                break
            actual = actual.siguiente 

def agregar_tarea_a_la_lista():
    lista_tareas = ListaDeTareas()

    while True:
        tarea = input("Ingrese la tarea (o 'salir' para terminar): ")
        if tarea.lower() == 'salir':
            break

        descripcion = input("Ingrese la descripción de la tarea: ")
        prioridad = int(input("Ingrese el nivel de prioridad (1 es alto, 2 es mediano, 3 es bajo): "))
        fecha_vencimiento = input("Ingrese la fecha de vencimiento (ejemplo: 2024-09-30): ")
     
        lista_tareas.agregar_tarea(descripcion, prioridad, fecha_vencimiento)

    return lista_tareas

lista_tareas = agregar_tarea_a_la_lista()

lista_tareas.mostrar_tareas()


