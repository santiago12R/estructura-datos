class Vehiculo :
     
    def __init__ (self,marca:str, combustible:str) :


        self.marca= marca
        self.combustible= combustible

    def  encender (self) :

        pass 

    def  arrancar (self): 
        pass
    
    def __str__(self) :

        return f"EL vehiculo es  {self.marca}, utiliza el combustible {self.combustible}"
    
carro = Vehiculo("toyota","corriente")

print(carro)    
print(type(carro))#--->es para mostrar la clase que esta guardada

class Moto (Vehiculo):

    def __init__(self,mar:str,comb:str) :
        super().__init__(mar,comb)#-->como es un hijo lo ponemos por parametro


class Carro(Vehiculo) :
    
    pass

motocicleta= Moto("Honda", "Corriente")

mi_carro= Carro ("mazda", "extra"   )

print(motocicleta)
print(mi_carro)


   #Crear una clase llamada Vehículo, esta clase debe recibir 2 parámetros, marca y combustible; la clase también debe contener dos métodos encender y arrancar. 
#Instanciar la clase y usar el método mágico __str__ para imprimir la marca y el combustible usado