class Moto (Vehiculo):

    def __init__(self,mar:str,comb:str) :
        super().__init__(mar,comb)


class Carro(Vehiculo) :
    
    pass

motocicleta= Moto("Honda", "Corriente")

mi_carro= Carro ("mazda", "extra"   )

print(motocicleta)
print(type(mi_carro))


#Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo. 
#Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado