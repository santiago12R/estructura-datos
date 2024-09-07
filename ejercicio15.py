#Realizar la multiplicacion de dos numeros por medio de sumas

def multiplicacion_suma(a:int, b:int )  :

    if  a == 0 :

        return 0
    
    return b + multiplicacion_suma(a-1,b)

print(multiplicacion_suma(4,5))


 

