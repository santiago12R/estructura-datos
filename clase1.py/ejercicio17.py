
class Vehiculo:
    def __init__(self, marca: str, combustible: str):
        self.marca = marca
        self.combustible = combustible

    def __str__(self):
        return f"Vehiculo de marca {self.marca} y usa {self.combustible} como combustible."


class Moto(Vehiculo):
    def __init__(self, marca: str, combustible: str):
        super().__init__(marca, combustible)


class Carro(Vehiculo):
    pass


motocicleta = Moto("Honda", "Corriente")
mi_carro = Carro("Mazda", "Extra")


print(motocicleta)
print(type(mi_carro))


#Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo. 
#Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado