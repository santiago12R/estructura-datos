#Clase Persona: Crea una clase Persona con atributos como nombre, edad y género. Incluye métodos para obtener y establecer los valores de estos atributos, así como un método presentarse() que imprima una breve descripción de la persona.
class Persona:
    def __init__(self, nombre, edad, genero):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
    
  
    def get_nombre(self):                             #Recuerda Los getters
                                                    # y setters permiten el control sobre cómo se accede y 
                                                     #modifica la información de los atributos.
        return self._nombre
    
    def get_edad(self):
        return self._edad
    
    def get_genero(self):
        return self._genero
    
    # Métodos para establecer los atributos
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_edad(self, edad):
        self._edad = edad
    
    def set_genero(self, genero):
        self._genero = genero
    
    # aqui ponemos Método para presentarse y como se va a poner en el print
    def presentarse(self):
        print(f"Hola, me llamo {self._nombre}, tengo {self._edad} años y soy {self._genero}.")

    

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
genero = input("Ingresa tu género: ")

persona1 = Persona(nombre, edad, genero)

# aqui esta la variable donde me  muestra lo que nos piden y como mostrarlo
persona1.presentarse()
