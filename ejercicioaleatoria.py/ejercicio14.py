def es_palindromo(palabra):
    palabra= palabra.lower()
    return palabra == palabra[::-1]

palabra=str(input("Introduce la palabra: "))
if es_palindromo(palabra):
    
    print("si es una palabra palindromo ")
else : 
    print("no es una palabra palindromo ")
        