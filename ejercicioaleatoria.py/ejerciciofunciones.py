def factorial(numero:int)-> str|int:
    
    resultado = 1
    if numero < 0 :

        return "no se puede valores negativos"
    
    elif  numero == 0 :

        return 1
    for n in range(1, numero+1) :
        resultado = resultado*n

    return resultado
    
while True:
    facto = factorial(int(input("Ingrese un numero para calcular su facotrial: ")))
    print("el resultado es:",facto,)

   
    
    