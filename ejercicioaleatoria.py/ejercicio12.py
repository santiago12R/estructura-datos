def operacion_basica(n1,n2,operacion):
    if operacion=='suma':
        return n1+n2
    elif operacion == 'resta' :
        return n1-n2
    elif operacion == 'multiplicacion ' :

        return n1*n2
    elif operacion == 'divison' :
         
         if n2 == 0 : 
            return "error division por cero"

    else :
        return n1/n2
    

n1=float(input("Digite un numero: "))
n2=float(input("Digite un numero: "))
operacion=input("Que operacion quiere realizar: ")

resultado = operacion_basica(n1,n2,operacion)
print("Su respuesta es: ", resultado)

    







    
